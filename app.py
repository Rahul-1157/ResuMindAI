import streamlit as st
from src.resumind.config import configure_gemini_api
from src.resumind.file_parser import get_text_from_file
from src.resumind.gemini_client import get_gemini_response
from src.resumind.prompts import SUMMARY_PROMPT, ATS_PROMPT, KEYWORDS_PROMPT, JD_MATCH_PROMPT_TEMPLATE
from src.resumind.styles import CSS_STYLE

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="ResuMind AI: Intelligent Resume Analyzer",
    page_icon="🧠",
    layout="wide",
)

# --- 2. App Styling ---
st.markdown(CSS_STYLE, unsafe_allow_html=True)

# --- 3. Sidebar ---
with st.sidebar:
    st.title("About ResuMind AI")
    st.markdown("""
    ResuMind AI leverages LLM to provide you with instant, intelligent feedback on your resume. 
    
    **How it works:**
    1.  **Upload**: Provide your resume in PDF or DOCX format.
    2.  **Process**: The app extracts the text content from your file.
    3.  **Analyze**: Gemini processes the text based on expert-crafted prompts.
    4.  **Review**: Get detailed insights across multiple tabs.
    
    Your data is not stored. The analysis happens in real-time for each session.
    """)
    st.markdown("---")
    st.markdown("Made with ❤️ by Pawan Sharma ") # Optional: Add your name or GitHub link

# --- 4. Main Application Logic ---
st.markdown("<h1 class='main-header'>ResuMind AI 🧠</h1>", unsafe_allow_html=True)
st.subheader("Your personal LLM-powered resume analysis and optimization tool")

# Check for API key at the start
api_key_configured = configure_gemini_api()

if not api_key_configured:
    # st.warning("⚠️ API Key not found. Please create a `.env` file in the root directory with your `GOOGLE_API_KEY` to use the app.", icon="🚨")
    pass
else:
    uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"], help="Upload your resume to get started.")

    if uploaded_file is not None:
        with st.spinner("Analyzing your resume... This might take a moment."):
            resume_text = get_text_from_file(uploaded_file)
        
        if not resume_text.startswith("Error:"):
            st.success("Resume uploaded and processed successfully!", icon="✅")

            # --- Analysis Tabs ---
            tab1, tab2, tab3, tab4 = st.tabs(["**📄 Resume Summary** ", "**🤖 ATS Report**", "**🔑 Keyword Analysis**", "**🎯 Job Description Match**"])

            with tab1:
                st.header("Professional Summary")
                st.write("Here is a concise summary of your resume, highlighting key strengths and experience.")
                with st.spinner("Generating summary..."):
                    summary_response = get_gemini_response(resume_text, SUMMARY_PROMPT)
                    st.markdown(summary_response)

            with tab2:
                st.header("Applicant Tracking System (ATS) Report")
                st.write("This report analyzes how well your resume is optimized for automated screening systems.")
                with st.spinner("Performing ATS analysis..."):
                    ats_response = get_gemini_response(resume_text, ATS_PROMPT)
                    st.markdown(ats_response)

            with tab3:
                st.header("Keyword & Skills Analysis")
                st.write("These are the most prominent skills and keywords extracted from your resume.")
                with st.spinner("Extracting keywords..."):
                    keywords_response = get_gemini_response(resume_text, KEYWORDS_PROMPT)
                    st.markdown(keywords_response)

            with tab4:
                st.header("Job Description Match Analysis")
                st.write("Paste a job description below to see how your resume aligns with the requirements.")
                job_description = st.text_area("Paste the Job Description here", height=300, placeholder="Enter the full job description here...")

                if st.button("Analyze Match", type="primary"):
                    if job_description:
                        with st.spinner("Comparing resume to job description..."):
                            jd_prompt = JD_MATCH_PROMPT_TEMPLATE.format(jd=job_description)
                            jd_match_response = get_gemini_response(resume_text, jd_prompt)
                            st.markdown(jd_match_response)
                    else:
                        st.warning("Please paste a job description to analyze the match.")
        else:
            # Display error from file processing
            st.error(resume_text, icon="❌")




