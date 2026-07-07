"""
agents/market_research.py
==========================
Agent 1 — Market Research Agent

This agent answers:
- How big is the market?
- Who are the target customers?
- What are the current trends?
- Is there demand for this business?
"""

from agents.base_agent import BaseAgent


MARKET_RESEARCH_PROMPT = """You are an expert Market Research Analyst with 15 years of experience.
Your job is to analyze the business idea and provide comprehensive market research.

Your analysis MUST include:
1. **Market Overview**: Size, growth rate, and potential
2. **Target Customer Profile**: Age, income, location, behavior, needs
3. **Market Trends**: Current trends supporting or challenging this business
4. **Demand Analysis**: Is there genuine demand? How strong?
5. **Market Entry Timing**: Is now a good time to enter?
6. **Key Opportunities**: Specific gaps in the market this business can fill

Be data-driven, specific to the Indian market context where relevant,
and always tie insights back to the specific business idea provided."""


class MarketResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Market Research Agent",
            system_prompt=MARKET_RESEARCH_PROMPT
        )


def run_market_research(business_idea: str) -> str:
    """Convenience function to run market research agent."""
    agent = MarketResearchAgent()
    return agent.run(business_idea)
