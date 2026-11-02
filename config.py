import os

from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY", "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")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")