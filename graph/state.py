"""
graph/state.py
==============
This defines the SHARED STATE for LangGraph.

Think of this as a "shared notepad" that every agent
can read from and write to as the workflow progresses.

When Agent 1 (Market Research) finishes, it writes its
result to this state. Agent 2 can see Agent 1's result
if needed, and so on.

By the end, the state has ALL outputs ready for synthesis.
"""

from typing import Optional
from typing_extensions import TypedDict


class BusinessAnalystState(TypedDict):
    """
    The shared state passed between all LangGraph nodes.
    
    Each field starts as None and gets filled as agents run.
    """

    # Input — set at the very beginning
    business_idea: str

    # Agent outputs — filled one by one as agents complete
    market_research: Optional[str]
    competitor_analysis: Optional[str]
    financial_plan: Optional[str]
    risk_analysis: Optional[str]
    marketing_strategy: Optional[str]

    # Final output — filled by the synthesizer at the end
    final_report: Optional[str]

    # Status tracking
    current_step: Optional[str]
    error: Optional[str]
