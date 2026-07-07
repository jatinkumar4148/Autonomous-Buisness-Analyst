"""
graph/nodes.py
==============
Each function here is a NODE in the LangGraph workflow.

A node = one step in the pipeline.
Each node:
1. Reads the current state
2. Does its job (runs an agent)
3. Updates the state with its result
4. Returns the updated state

LangGraph then passes the updated state to the next node.
"""

from graph.state import BusinessAnalystState
from agents.market_research import run_market_research
from agents.competitor_analysis import run_competitor_analysis
from agents.financial_planner import run_financial_planner
from agents.risk_analysis import run_risk_analysis
from agents.marketing_strategy import run_marketing_strategy
from agents.synthesizer import synthesize_business_plan


def market_research_node(state: BusinessAnalystState) -> BusinessAnalystState:
    """Node 1: Run market research agent"""
    try:
        result = run_market_research(state["business_idea"])
        return {
            **state,
            "market_research": result,
            "current_step": "market_research_done"
        }
    except Exception as e:
        return {**state, "error": f"Market Research failed: {str(e)}"}


def competitor_analysis_node(state: BusinessAnalystState) -> BusinessAnalystState:
    """Node 2: Run competitor analysis agent"""
    try:
        result = run_competitor_analysis(state["business_idea"])
        return {
            **state,
            "competitor_analysis": result,
            "current_step": "competitor_analysis_done"
        }
    except Exception as e:
        return {**state, "error": f"Competitor Analysis failed: {str(e)}"}


def financial_planner_node(state: BusinessAnalystState) -> BusinessAnalystState:
    """Node 3: Run financial planner agent"""
    try:
        result = run_financial_planner(state["business_idea"])
        return {
            **state,
            "financial_plan": result,
            "current_step": "financial_plan_done"
        }
    except Exception as e:
        return {**state, "error": f"Financial Planner failed: {str(e)}"}


def risk_analysis_node(state: BusinessAnalystState) -> BusinessAnalystState:
    """Node 4: Run risk analysis agent"""
    try:
        result = run_risk_analysis(state["business_idea"])
        return {
            **state,
            "risk_analysis": result,
            "current_step": "risk_analysis_done"
        }
    except Exception as e:
        return {**state, "error": f"Risk Analysis failed: {str(e)}"}


def marketing_strategy_node(state: BusinessAnalystState) -> BusinessAnalystState:
    """Node 5: Run marketing strategy agent"""
    try:
        result = run_marketing_strategy(state["business_idea"])
        return {
            **state,
            "marketing_strategy": result,
            "current_step": "marketing_strategy_done"
        }
    except Exception as e:
        return {**state, "error": f"Marketing Strategy failed: {str(e)}"}


def synthesizer_node(state: BusinessAnalystState) -> BusinessAnalystState:
    """Node 6: Combine all outputs into final business plan"""
    try:
        final_report = synthesize_business_plan(
            business_idea=state["business_idea"],
            market_research=state.get("market_research", "Not available"),
            competitor_analysis=state.get("competitor_analysis", "Not available"),
            financial_plan=state.get("financial_plan", "Not available"),
            risk_analysis=state.get("risk_analysis", "Not available"),
            marketing_strategy=state.get("marketing_strategy", "Not available"),
        )
        return {
            **state,
            "final_report": final_report,
            "current_step": "complete"
        }
    except Exception as e:
        return {**state, "error": f"Synthesizer failed: {str(e)}"}
