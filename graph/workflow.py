"""
graph/workflow.py
=================
This is where LangGraph builds the actual workflow pipeline.

Think of this as drawing the MAP of how agents connect:

START
  ↓
market_research_node
  ↓
competitor_analysis_node
  ↓
financial_planner_node
  ↓
risk_analysis_node
  ↓
marketing_strategy_node
  ↓
synthesizer_node
  ↓
END

LangGraph manages the state automatically between each step.
"""

from langgraph.graph import StateGraph, END
from graph.state import BusinessAnalystState
from graph.nodes import (
    market_research_node,
    competitor_analysis_node,
    financial_planner_node,
    risk_analysis_node,
    marketing_strategy_node,
    synthesizer_node,
)


def build_workflow():
    """
    Builds and compiles the LangGraph workflow.
    
    Returns a compiled graph that can be invoked with
    an initial state to run the full pipeline.
    """

    # Step 1: Create the graph with our state schema
    workflow = StateGraph(BusinessAnalystState)

    # Step 2: Add all agent nodes to the graph
    workflow.add_node("market_research",     market_research_node)
    workflow.add_node("competitor_analysis", competitor_analysis_node)
    workflow.add_node("financial_planner",   financial_planner_node)
    workflow.add_node("risk_analysis",       risk_analysis_node)
    workflow.add_node("marketing_strategy",  marketing_strategy_node)
    workflow.add_node("synthesizer",         synthesizer_node)

    # Step 3: Define the EDGES (flow between nodes)
    # This is what makes it a graph — each edge = "go here next"
    workflow.set_entry_point("market_research")

    workflow.add_edge("market_research",     "competitor_analysis")
    workflow.add_edge("competitor_analysis", "financial_planner")
    workflow.add_edge("financial_planner",   "risk_analysis")
    workflow.add_edge("risk_analysis",       "marketing_strategy")
    workflow.add_edge("marketing_strategy",  "synthesizer")
    workflow.add_edge("synthesizer",         END)

    # Step 4: Compile the graph into a runnable app
    app = workflow.compile()

    return app


# Pre-built workflow — import this in main.py
business_analyst_workflow = build_workflow()
