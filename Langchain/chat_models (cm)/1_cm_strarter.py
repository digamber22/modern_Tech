# open ai model
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4")

result = llm.invoke("What is the current time in India?")

print(result)

# or we can use gemini pro model ; 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read API key and model name from environment
api_key = os.getenv("GEMINI_API_KEY")
model_name = os.getenv("GEMINI_MODEL_NAME", "gemma-3-12b-it")  # default if not set

# Validate API key
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please set it in your .env file.")

# Initialize the model
llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key, temperature=0.7)

# Send a prompt
result = llm.invoke("what is langchain?")

# Print the result (usually result.content)
print(result.content if hasattr(result, "content") else result)
