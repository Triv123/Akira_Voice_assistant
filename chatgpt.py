from openai import OpenAI
from dotenv import load_dotenv
import os
import traceback

load_dotenv()

def aiProcess(command):
    print("[DEBUG] Starting aiProcess...")

    api_key = os.getenv("ChatGPT_KEY")
    if not api_key:
        print("❌ ERROR: ChatGPT_KEY not found in .env file!")
        return "Missing API key."

    print("[DEBUG] API key loaded.")
    
    try:
        client = OpenAI(api_key=api_key)

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4o" if available
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Akira skilled in general tasks. Be brief."},
                {"role": "user", "content": command}
            ],
            timeout=15  # optional, avoids hanging
        )

        return completion.choices[0].message.content

    except Exception as e:
        return "Session expired try other features"

