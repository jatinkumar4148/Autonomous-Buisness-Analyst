"""
rag/loader.py
=============
This module loads documents and splits them into small chunks.

Think of it like this:
- You have a big textbook (business knowledge)
- This module cuts it into small paragraphs
- So the AI can quickly find the relevant paragraph when needed
"""

import os
from typing import List
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def load_documents(data_dir: str = None) -> List[Document]:
    """
    Loads all .txt files from the data directory.
    Returns a list of Document objects.
    """
    if data_dir is None:
        # Default to the data/ folder in project root
        data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
        data_dir = os.path.abspath(data_dir)

    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found: {data_dir}")

    print(f"📂 Loading documents from: {data_dir}")

    loader = DirectoryLoader(
        data_dir,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )

    documents = loader.load()
    print(f"✅ Loaded {len(documents)} document(s)")
    return documents


def split_documents(documents: List[Document]) -> List[Document]:
    """
    Splits large documents into smaller overlapping chunks.
    
    Why overlap? So important sentences at chunk boundaries
    are not lost — context flows across chunks.
    
    chunk_size=800:  Each chunk is ~800 characters
    chunk_overlap=100: 100 chars shared between chunks
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " "],
    )

    chunks = splitter.split_documents(documents)
    print(f"✅ Split into {len(chunks)} chunks")
    return chunks


def load_and_split(data_dir: str = None) -> List[Document]:
    """
    Convenience function: load + split in one call.
    This is what the RAG retriever calls at startup.
    """
    documents = load_documents(data_dir)
    chunks = split_documents(documents)
    return chunks
