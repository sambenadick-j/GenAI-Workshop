from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq

# task 1: add optional params to create_llm_model and add in function description
# task 2: import from respective package and return model instance

def create_llm_model():
    # optional params
    model=ChatGroq(
         model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2
    )
    return model
    """
    Creates and returns a configured instance of the model.

    Args:
        explain about the params

    Returns:
        Configured model instance
    """
    
    # todo

