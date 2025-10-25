import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

def get_gemini_response(input_text: str, prompt: str) -> str:
    """
    Calls the Gemini model to get a response for the given input and prompt.
    Prefers LangChain (ChatGoogleGenerativeAI).
    Args:
        input_text (str): The text content from the resume.
        prompt (str): The instruction/prompt for the Gemini model.
    Returns:
        str: The generated response from the Gemini model or an error message.
    """
    try:
        # Compose the simple message the same way other parts of your app expect.
        composed = f"{prompt}\n\nResume Content:\n{input_text}"
        # LangChain's Google integration uses the GOOGLE_API_KEY environment variable.
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.4)
        message = HumanMessage(content=composed)
        lc_response = llm([message])

        # LangChain response object exposes .content (string)
        if lc_response and hasattr(lc_response, "content") and lc_response.content:
            return lc_response.content.strip()

    except Exception as e:
        return f"Error: Unexpected error while getting Gemini response. Details: {e}"




