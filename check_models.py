import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    # Fallback to a placeholder or ask input (but here we just print warning)
    print("Warning: GEMINI_API_KEY not found in environment.")
    # You might want to hardcode a key for testing if you have one, or just exit.
else:
    genai.configure(api_key=api_key)
    try:
        print(f"Using API Key: {api_key[:5]}...")
        print("Available models for generateContent:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"- {m.name}")
    except Exception as e:
        print(f"Error: {e}")
