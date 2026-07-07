"""
agents/base_agent.py
====================
This is the BASE agent — a template that all 5 agents inherit from.

Think of it as a "base employee contract" — every agent:
1. Gets a role (Market Researcher, Financial Planner, etc.)
2. Retrieves relevant context from RAG
3. Sends a prompt to Mistral LLM
4. Returns the structured response

All 5 agents just customize their role and prompt.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.llm import get_llm
from rag.retriever import retrieve_context


class BaseAgent:
    """
    Base class for all business analyst agents.
    Each agent inherits this and provides its own system_prompt.
    """

    def __init__(self, role: str, system_prompt: str):
        """
        Args:
            role: Human-readable name of this agent (e.g. "Market Research Agent")
            system_prompt: The instruction that defines what this agent does
        """
        self.role = role
        self.system_prompt = system_prompt
        self.llm = get_llm(temperature=0.4)
        self.output_parser = StrOutputParser()

    def run(self, business_idea: str) -> str:
        """
        Main method to run the agent.
        
        Steps:
        1. Retrieve relevant context from RAG vector store
        2. Build the prompt with context + business idea
        3. Send to Mistral LLM
        4. Return the parsed response
        """
        print(f"🤖 Running: {self.role}...")

        # Step 1: Get relevant knowledge from RAG
        rag_context = retrieve_context(
            query=f"{self.role} for {business_idea}",
            k=4
        )

        # Step 2: Build prompt template
        prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                self.system_prompt + "\n\nAlways provide specific, actionable insights. "
                "Format your response with clear sections and bullet points."
            ),
            (
                "human",
                """Business Idea: {business_idea}

Relevant Knowledge Base Context:
{rag_context}

Based on the business idea and the context above, provide your detailed analysis.
Be specific, practical, and tailored to this exact business idea."""
            )
        ])

        # Step 3: Create chain — Prompt → LLM → Parser
        chain = prompt | self.llm | self.output_parser

        # Step 4: Run and return
        response = chain.invoke({
            "business_idea": business_idea,
            "rag_context": rag_context,
        })

        print(f"✅ {self.role} completed!")
        return response
