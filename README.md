# 🧠 ResuMind AI: Intelligent Resume Analyzer 🚀

**ResuMind AI** is a powerful, user-friendly web application designed to help job seekers optimize their resumes.  
By leveraging **LLM via LangChain**, this tool provides an in-depth analysis of your resume, giving you the insights needed to stand out in today’s competitive job market.

---

## ✨ Features

- **📄 Multi-Format Upload:** Upload your resume in either **PDF** or **DOCX** format.
- **🤖 LLM-Powered Summary:** Get a quick, professional summary of your resume, highlighting your key strengths and experience.
- **📊 ATS Compatibility Check:** Receive an **Applicant Tracking System (ATS)** compatibility score out of 100, with actionable advice to improve your resume's machine-readability.
- **🔑 Keyword Analysis:** Extract relevant skills and keywords from your resume, helping you align it with job descriptions.
- **🧩 Job Description Matching:** Paste a job description to see how well your resume matches the requirements, complete with a **percentage score** and detailed comparison.
- **🔒 Secure & Private:** Your API key is loaded locally, and your resume data is processed in memory for the duration of the session. Nothing is stored.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM Model:** Google Gemini 2.5 Flash via **LangChain** 
- **LangChain Wrapper:** `langchain-google-genai`  
- **File Processing:** `PyPDF2` (for PDFs), `python-docx` (for DOCX files)  
- **Environment Management:** `python-dotenv`

---
