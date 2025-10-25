# src/resumind/file_parser.py
from PyPDF2 import PdfReader
from docx import Document
import io

def get_text_from_file(uploaded_file):
    """
    Extracts text from an uploaded file (PDF or DOCX).
    Args:
        uploaded_file: A file-like object from Streamlit's file_uploader.
    Returns:
        str: The extracted text or an error message.
    """
    text = ""
    file_name = uploaded_file.name
    
    # Use io.BytesIO to handle the uploaded file in memory
    file_stream = io.BytesIO(uploaded_file.getvalue())

    if file_name.endswith('.pdf'):
        try:
            pdf_reader = PdfReader(file_stream)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
        except Exception as e:
            return f"Error: Could not read the PDF file. It might be corrupted or protected. Details: {e}"

    elif file_name.endswith('.docx'):
        try:
            doc = Document(file_stream)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            return f"Error: Could not read the DOCX file. Details: {e}"
            
    else:
        return "Error: Unsupported file format. Please upload a PDF or DOCX file."
        
    return text