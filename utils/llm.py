"""
utils/llm.py
============
This module sets up the Mistral LLM and Embeddings.
Think of this as the "brain connector" — every agent
uses this to talk to Mistral AI.
"""

import os
import time
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings

# Load .env file so MISTRAL_API_KEY is available
load_dotenv()


def get_llm(temperature: float = 0.3) -> ChatMistralAI:
    """
    Returns a Mistral LLM instance.
    
    - model: mistral-medium-latest (smart + affordable)
    - temperature: 0.3 = focused answers (0=robotic, 1=creative)
    """
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError(
            "MISTRAL_API_KEY not found!\n"
            "Please create a .env file and add: MISTRAL_API_KEY=your_key_here\n"
            "Get your free key at: https://console.mistral.ai"
        )

    return ChatMistralAI(
        model=os.getenv("MISTRAL_MODEL", "mistral-small-latest"),
        mistral_api_key=api_key,
        temperature=temperature,
    )


def invoke_with_retry(chain, payload, operation: str):
    """Retry transient Mistral rate-limit and availability responses."""
    delays = (15, 30, 60, 90)
    for attempt, delay in enumerate((0, *delays), start=1):
        if delay:
            print(f"⏳ {operation} temporarily unavailable; retrying in {delay} seconds...")
            time.sleep(delay)
        try:
            return chain.invoke(payload)
        except Exception as exc:
            error_text = str(exc).lower()
            is_transient = any(
                marker in error_text
                for marker in ("429", "502", "503", "504", "rate limit", "temporarily unavailable")
            )
            if not is_transient or attempt == len(delays) + 1:
                raise


def get_embeddings() -> MistralAIEmbeddings:
    """
    Returns Mistral Embeddings instance.
    Used by FAISS to convert text into numbers for search.
    """
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY not found in .env file!")

    return MistralAIEmbeddings(
        model="mistral-embed",
        mistral_api_key=api_key,
    )
