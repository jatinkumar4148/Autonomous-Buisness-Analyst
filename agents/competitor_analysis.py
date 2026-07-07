"""
agents/competitor_analysis.py
==============================
Agent 2 — Competitor Analysis Agent

This agent answers:
- Who are the main competitors?
- What are their strengths and weaknesses?
- Where are the gaps we can exploit?
- How should we position against them?
"""

from agents.base_agent import BaseAgent


COMPETITOR_ANALYSIS_PROMPT = """You are an expert Business Strategy Analyst specializing in
competitive intelligence and market positioning.

Your job is to analyze competitors for the given business idea.

Your analysis MUST include:
1. **Direct Competitors**: Who are they? What do they offer?
2. **Indirect Competitors**: Alternative solutions customers might use
3. **SWOT Analysis**: Competitors' Strengths, Weaknesses, Opportunities, Threats
4. **Competitive Gaps**: What are competitors NOT doing well?
5. **Differentiation Strategy**: How can this new business stand out?
6. **Competitive Advantage**: What unique value can this business offer?
7. **Pricing Benchmark**: What are competitors charging?

Be specific about real companies/brands where applicable.
Focus on actionable insights the business owner can use immediately."""


class CompetitorAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role="Competitor Analysis Agent",
            system_prompt=COMPETITOR_ANALYSIS_PROMPT
        )


def run_competitor_analysis(business_idea: str) -> str:
    """Convenience function to run competitor analysis agent."""
    agent = CompetitorAnalysisAgent()
    return agent.run(business_idea)
