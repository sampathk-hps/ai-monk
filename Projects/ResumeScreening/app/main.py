from core.pdf_loader import get_pdf_content
from core.docx_loader import get_docx_content
from core.txt_loader import get_txt_content
from core.llm import get_llm
from constants.constants import PROMPT_DIR
from core.chroma_db_handler import store_content

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import streamlit as st
import os
import re
import logging
import tempfile

logging.basicConfig(level=logging.INFO)


# Extract text from uploaded files
def extract_text_from_resume(file) -> str:
    file_extension = os.path.splitext(file.name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp:
        tmp.write(file.getbuffer())
        temp_file_path = tmp.name

    try:
        if file_extension == '.pdf':
            content = get_pdf_content(temp_file_path)
        elif file_extension == '.docx':
            content = get_docx_content(temp_file_path)
        elif file_extension == '.txt':
            content = get_txt_content(temp_file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

        return content
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)


# Extract percentage score from analysis text
def extract_suitability_score(text):
    match = re.search(r"Suitability Score: (\d{1,3})%", text)
    if match:
        return int(match.group(1))
    return None

def _get_prompt_template() -> PromptTemplate:
    with open(PROMPT_DIR, 'r') as f:
        template_content = f.read()
    prompt_template = PromptTemplate(
        input_variables=["job_requirements", "resume_text"],
        template=template_content
    )
    return prompt_template

def start_analysis(job_requirements: str, resume_text: str) -> str:
    llm = get_llm()
    prompt_template = _get_prompt_template()
    parser = StrOutputParser()

    chain = prompt_template | llm | parser
    
    if not job_requirements or not resume_text:
        return "Please provide both job requirements and resume text."
    
    analysis = chain.invoke(input={
        "job_requirements": job_requirements,
        "resume_text": resume_text
    })

    return analysis


def streamlit_app():
    st.set_page_config(page_title="Resume Screening App", layout="wide")
    st.title("Resume Screening with LCEL and Vector Store")

    col1, col2 = st.columns(2)
    with col1:
        st.header("Job Requirements")
        job_requirements = st.text_area("Enter job requirements", height=300)
    with col2:
        st.header("Upload Resume")
        uploaded_file = st.file_uploader("Upload a resume", type=["pdf", "docx", "txt"])

    if st.button("Analyze") and uploaded_file and job_requirements:
        with st.spinner("Analyzing..."):
            resume_content = extract_text_from_resume(uploaded_file)

            if not resume_content or not resume_content.strip():
                st.error("Failed to extract content from resume")
                return

            with st.expander("View Resume Content"):
                st.text(resume_content)
            
            analysis = start_analysis(job_requirements, resume_content)

            st.header("AI Analysis")
            st.markdown(analysis)

            # Extract and display the suitability score
            suitability_score = extract_suitability_score(analysis)
            if suitability_score is not None:
                st.metric(label="Resume Suitability Score", value=f"{suitability_score}%")
            else:
                st.warning("Analysis Done.")

            store_content(resume_content, os.path.splitext(uploaded_file.name)[0])
            st.success("Analysis stored in vector database.")

            st.download_button("Download Analysis", analysis, file_name="resume_analysis.txt")


if __name__ == "__main__":
    streamlit_app()