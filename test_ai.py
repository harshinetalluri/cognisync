
import asyncio
import os
import sys
from dotenv import load_dotenv

load_dotenv(dotenv_path='backend/.env') # Loading before importing app

# Add current directory to path so we can import app
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from app.services.ai_service import ai_service

async def main():
    print("Testing AI Service...")
    api_key = os.getenv("GOOGLE_API_KEY")
    print(f"API Key present: {bool(api_key)}")
    if api_key:
        print(f"API Key start: {api_key[:5]}...")

    try:
        questions = await ai_service.generate_questions("Photosynthesis", "Medium")
        print(f"Successfully generated {len(questions)} questions.")
        for q in questions:
            print(f"- {q.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
