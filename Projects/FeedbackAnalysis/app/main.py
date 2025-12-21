import pandas as pd
from core.csv_loader import load_and_normalize_data
from graphs.feedback_graph import build_feedback_graph
from constants.constants import OUTPUT_TICKETS_PATH

import logging
logging.basicConfig(level=logging.INFO)

def run_batch_processing():
    logging.info("Loading data...")
    raw_data = load_and_normalize_data()
    
    logging.info(f"Initializing Graph... Processing {len(raw_data)} items.")
    app = build_feedback_graph()
    
    results = []
    
    for item in raw_data:
        # Initialize state for this specific item
        initial_state = {"current_item": item}
        
        # Run graph
        output = app.invoke(initial_state) # type: ignore
        
        # Extract ticket
        if "final_ticket" in output:
            results.append(output["final_ticket"].model_dump())
            logging.info(f"Processed {item.source_id} -> {output['final_ticket'].category}")

    # Save to CSV
    if results:
        df = pd.DataFrame(results)
        df.to_csv(OUTPUT_TICKETS_PATH, index=False)
        logging.info(f"Success. Tickets saved to {OUTPUT_TICKETS_PATH}")

if __name__ == "__main__":
    run_batch_processing()
