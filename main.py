"""
main.py
=======
ENTRY POINT — Run this file to start the Business Analyst AI.

Usage:
    python main.py

What happens when you run this:
1. You type your business idea
2. RAG vector store is built from knowledge base
3. LangGraph starts the 6-node pipeline
4. All 5 agents run sequentially
5. Final synthesizer creates the full business plan
6. Plan is printed to screen AND saved as a .txt file
"""

import os
import sys
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()


def print_banner():
    """Prints a welcome banner."""
    print("\n" + "=" * 65)
    print("  🤖  AUTONOMOUS BUSINESS ANALYST AI")
    print("  Powered by: Mistral + LangChain + LangGraph + RAG")
    print("=" * 65 + "\n")


def print_section(title: str, content: str):
    """Prints a formatted section."""
    print(f"\n{'─' * 65}")
    print(f"  {title}")
    print(f"{'─' * 65}")
    print(content)


def save_report(business_idea: str, report: str) -> str:
    """
    Saves the final business plan to a .txt file.
    Returns the filename.
    """
    # Create output folder if it doesn't exist
    os.makedirs("outputs", exist_ok=True)

    # Create a safe filename from the business idea
    safe_name = "".join(
        c if c.isalnum() or c in (" ", "_") else "_"
        for c in business_idea[:40]
    ).strip().replace(" ", "_")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/business_plan_{safe_name}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"BUSINESS PLAN: {business_idea.upper()}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 65 + "\n\n")
        f.write(report)

    return filename


def run_business_analyst(business_idea: str):
    """
    Main function that runs the full AI pipeline.
    
    Args:
        business_idea: User's business idea string
    """

    print(f"\n📋 Business Idea: {business_idea}")
    print("\n⏳ Starting analysis pipeline...\n")

    start_time = time.time()

    # ─── Step 1: Initialize RAG vector store ───────────────────
    print("─" * 65)
    print("  MODULE 1/3 — Building RAG Knowledge Base")
    print("─" * 65)

    # Import here so RAG builds only when needed
    from rag.retriever import get_vector_store
    get_vector_store()  # Builds and caches the FAISS store

    # ─── Step 2: Run LangGraph pipeline ────────────────────────
    print("\n" + "─" * 65)
    print("  MODULE 2/3 — Running 5 AI Agents via LangGraph")
    print("─" * 65 + "\n")

    from graph.workflow import business_analyst_workflow

    # Set initial state
    initial_state = {
        "business_idea": business_idea,
        "market_research": None,
        "competitor_analysis": None,
        "financial_plan": None,
        "risk_analysis": None,
        "marketing_strategy": None,
        "final_report": None,
        "current_step": "starting",
        "error": None,
    }

    # Run the full LangGraph workflow
    final_state = business_analyst_workflow.invoke(initial_state)

    # Check for errors
    if final_state.get("error"):
        print(f"\n❌ Pipeline error: {final_state['error']}")
        sys.exit(1)

    # ─── Step 3: Display and Save Results ───────────────────────
    print("\n" + "─" * 65)
    print("  MODULE 3/3 — Results Ready!")
    print("─" * 65)

    elapsed = round(time.time() - start_time, 1)

    # Print individual agent results
    sections = [
        ("📊 MARKET RESEARCH",     "market_research"),
        ("⚔️  COMPETITOR ANALYSIS", "competitor_analysis"),
        ("💰 FINANCIAL PLAN",      "financial_plan"),
        ("⚠️  RISK ANALYSIS",       "risk_analysis"),
        ("📣 MARKETING STRATEGY",  "marketing_strategy"),
    ]

    for title, key in sections:
        content = final_state.get(key, "Not available")
        if content:
            print_section(title, content)

    # Print the final synthesized plan
    print("\n" + "=" * 65)
    print("  🏆  FINAL BUSINESS PLAN (SYNTHESIZED)")
    print("=" * 65)
    print(final_state.get("final_report", "Final report not generated."))

    # Save to file
    filename = save_report(business_idea, final_state.get("final_report", ""))
    print(f"\n\n✅ Business plan saved to: {filename}")
    print(f"⏱️  Total time: {elapsed} seconds")
    print("\n" + "=" * 65 + "\n")


def main():
    """Main entry point."""
    print_banner()

    # Check API key before doing anything
    if not os.getenv("MISTRAL_API_KEY"):
        print("❌ ERROR: MISTRAL_API_KEY not found!")
        print("\nTo fix this:")
        print("  1. Create a file named .env in the project folder")
        print("  2. Add this line:  MISTRAL_API_KEY=your_key_here")
        print("  3. Get your free key at: https://console.mistral.ai")
        print("\nThen run python main.py again.\n")
        sys.exit(1)

    # Get business idea from user
    print("What business do you want to start?")
    print("Examples:")
    print("  • I want to open a coffee shop in Delhi")
    print("  • I want to start an online clothing store")
    print("  • I want to launch a fitness app")
    print("  • I want to open a bakery in Mumbai\n")

    business_idea = input("👉 Enter your business idea: ").strip()

    if not business_idea:
        print("❌ Please enter a business idea.")
        sys.exit(1)

    # Run the pipeline
    run_business_analyst(business_idea)


if __name__ == "__main__":
    main()
