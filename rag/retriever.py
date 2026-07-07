"""
rag/retriever.py
================
This module builds the FAISS vector store and retrieves
relevant context for any query.

Think of it like this:
- All document chunks are converted to numbers (vectors)
- FAISS stores all these numbers in a searchable database
- When an agent asks a question, FAISS finds the most
  similar chunks and returns them as context

This is the RAG (Retrieval Augmented Generation) magic!
"""

import os
from typing import List, Optional
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from utils.llm import get_embeddings
from rag.loader import load_and_split


# Cache the vector store so we don't rebuild it every time
_vector_store: Optional[FAISS] = None


def build_vector_store(data_dir: str = None) -> FAISS:
    """
    Builds the FAISS vector store from documents.
    
    Steps:
    1. Load and split documents into chunks
    2. Convert each chunk into a vector (embedding)
    3. Store all vectors in FAISS for fast similarity search
    """
    global _vector_store

    print("\n🔧 Building RAG vector store...")
    chunks = load_and_split(data_dir)

    print("🧠 Creating embeddings with Mistral (this may take a moment)...")
    embeddings = get_embeddings()

    _vector_store = FAISS.from_documents(chunks, embeddings)
    print("✅ Vector store ready!\n")

    return _vector_store


def get_vector_store(data_dir: str = None) -> FAISS:
    """
    Returns the vector store, building it if not already built.
    Uses caching so it only builds once per session.
    """
    global _vector_store
    if _vector_store is None:
        _vector_store = build_vector_store(data_dir)
    return _vector_store


def retrieve_context(query: str, k: int = 4) -> str:
    """
    Retrieves the top-k most relevant document chunks for a query.
    Returns them as a single string to inject into agent prompts.
    
    Args:
        query: The question or topic to search for
        k: Number of chunks to retrieve (default: 4)
    
    Returns:
        A formatted string of relevant context
    """
    store = get_vector_store()
    
    # Similarity search — finds k most relevant chunks
    docs: List[Document] = store.similarity_search(query, k=k)

    if not docs:
        return "No relevant context found."

    # Format chunks into a readable string
    context_parts = []
    for i, doc in enumerate(docs, 1):
        context_parts.append(f"[Context {i}]:\n{doc.page_content.strip()}")

    return "\n\n".join(context_parts)
