"""
utils/llm.py
============
This module sets up the Mistral LLM and Embeddings.
Think of this as the "brain connector" — every agent
uses this to talk to Mistral AI.
"""

import os
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
        model="mistral-medium-latest",
        mistral_api_key=api_key,
        temperature=temperature,
    )


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
