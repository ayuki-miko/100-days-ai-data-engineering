
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API keys
gemini = os.getenv("GEMINI_API_KEY")
groq = os.getenv("GROQ_API_KEY")
openai = os.getenv("OPENAI_API_KEY")

# Check whether keys exist
print("Gemini:", "Loaded" if gemini else "Missing")
print("Groq:", "Loaded" if groq else "Missing")
print("OpenAI:", "Loaded" if openai else "Missing")
