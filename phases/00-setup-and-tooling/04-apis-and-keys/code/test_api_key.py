import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Pull the key
api_key = os.getenv("OPENAI_API_KEY")

if api_key and api_key.startswith("sk-"):
    print("✅ SUCCESS: API key loaded securely!")
    print(f"Key starts with: {api_key[:10]}... (truncated for safety)")
else:
    print("❌ Key not found or .env not loaded correctly")