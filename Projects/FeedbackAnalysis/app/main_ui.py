import streamlit as st
import pandas as pd
import os
from core.csv_loader import load_and_normalize_data
from graphs.feedback_graph import build_feedback_graph
from constants.constants import INPUT_REVIEWS_PATH, INPUT_EMAILS_PATH, OUTPUT_TICKETS_PATH

# Page Config
st.set_page_config(page_title="Feedback Analysis AI", layout="wide")
st.title("Intelligent User Feedback Analysis")

# File Upload Section
st.subheader("Data Ingestion")
col1, col2 = st.columns(2)

with col1:
    uploaded_reviews = st.file_uploader("Upload App Store Reviews (CSV)", type=["csv"])
    
with col2:
    uploaded_emails = st.file_uploader("Upload Support Emails (CSV)", type=["csv"])

# Function to save uploaded file to the path expected by csv_loader.py
def save_uploaded_file(uploaded_file, destination_path):
    # Create directory if not exists
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    with open(destination_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

# Conditional Analysis Button
# We check if at least one file is present
can_proceed = uploaded_reviews is not None or uploaded_emails is not None

if can_proceed:
    if st.button("Start Analysis", type="primary"):
        
        # Save files to disk so core/csv_loader.py can find them
        if uploaded_reviews:
            save_uploaded_file(uploaded_reviews, INPUT_REVIEWS_PATH)
            st.toast("Reviews loaded successfully!", icon="✅")
            
        if uploaded_emails:
            save_uploaded_file(uploaded_emails, INPUT_EMAILS_PATH)
            st.toast("Emails loaded successfully!", icon="✅")

        # Processing & Logging
        st.divider()
        st.subheader("Processing Logs")
        
        # Create an expandable log container
        log_expander = st.expander("Live Agent Execution Logs", expanded=True)
        log_container = log_expander.container()
        log_container.markdown("initializing system...")
        
        # Load Data
        with st.spinner("Normalizing data..."):
            try:
                raw_data = load_and_normalize_data()
            except Exception as e:
                st.error(f"Error loading data: {e}")
                st.stop()
        
        if not raw_data:
            st.warning("No valid data found in uploaded files.")
            st.stop()

        # Initialize Graph
        app = build_feedback_graph()
        results = []
        
        # Progress Bar
        progress_bar = st.progress(0)
        total_items = len(raw_data)
        
        # Fixed height scrollable area for logs
        log_text = ""
        log_placeholder = log_container.empty()

        for i, item in enumerate(raw_data):
            initial_state = {"current_item": item}
            
            # Update Log
            log_text += f"\n\n**Processing Item: {item.source_id}** ({item.source_type})\n"
            log_placeholder.markdown(f"<div style='height: 300px; overflow-y: scroll;'>{log_text}</div>", unsafe_allow_html=True)
            
            # Stream events from the graph to show node activity
            try:
                for event in app.stream(initial_state):
                    for node_name, node_output in event.items():
                        # Extract specific details based on node
                        details = ""
                        if "classification" in node_output:
                            details = f"Classified as: **{node_output['classification']['category']}**"
                        elif "analysis" in node_output:
                            details = f"Priority: **{node_output['analysis']['priority']}**"
                        elif "validation" in node_output:
                            score = node_output['validation'].get('accuracy_score', 'N/A')
                            details = f"Validation Score: **{score}**"
                        elif "final_ticket" in node_output:
                            tkt = node_output['final_ticket']
                            results.append(tkt.model_dump())
                            details = "Ticket Created."

                        # Append to log
                        log_entry = f"   - **{node_name}**: {details}"
                        log_text += f"{log_entry}\n"
                        # Update the scrollable view
                        log_placeholder.markdown(f"<div style='height: 300px; overflow-y: scroll;'>{log_text}</div>", unsafe_allow_html=True)
                        
            except Exception as e:
                log_text += f"   - Error: {str(e)}\n"
                log_placeholder.markdown(f"<div style='height: 300px; overflow-y: scroll;'>{log_text}</div>", unsafe_allow_html=True)

            # Update progress
            progress_bar.progress((i + 1) / total_items)

        # Results Display
        st.success("Analysis Complete!")
        
        if results:
            df_results = pd.DataFrame(results)
            
            # Save to CSV as per requirement
            df_results.to_csv(OUTPUT_TICKETS_PATH, index=False)
            
            st.divider()
            st.subheader("Analysis Results")
            st.dataframe(df_results, use_container_width=True)
            
            # Download Button
            csv = df_results.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Tickets CSV",
                data=csv,
                file_name="generated_tickets.csv",
                mime="text/csv",
            )
        else:
            st.warning("No tickets were generated.")

else:
    st.info("Please upload at least one CSV file to enable analysis.")
