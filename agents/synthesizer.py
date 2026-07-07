"""
agents/synthesizer.py
======================
Final Synthesizer Agent

This is the LAST step — it takes ALL 5 agent outputs
and combines them into one polished, professional
business plan document.

Think of it as the "Editor-in-Chief" who takes all the
expert reports and writes the final document.
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from utils.llm import get_llm


def synthesize_business_plan(
    business_idea: str,
    market_research: str,
    competitor_analysis: str,
    financial_plan: str,
    risk_analysis: str,
    marketing_strategy: str,
) -> str:
    """
    Takes all 5 agent outputs and creates the final business plan.
    
    Args:
        business_idea: The original user input
        market_research: Output from Market Research Agent
        competitor_analysis: Output from Competitor Analysis Agent
        financial_plan: Output from Financial Planner Agent
        risk_analysis: Output from Risk Analysis Agent
        marketing_strategy: Output from Marketing Strategy Agent
    
    Returns:
        A complete, formatted business plan as a string
    """
    print("📝 Synthesizer: Creating final business plan...")

    llm = get_llm(temperature=0.3)
    output_parser = StrOutputParser()

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a Senior Business Consultant and Report Writer.
Your job is to synthesize multiple expert analyses into one
cohesive, professional business plan document.

The document should:
- Flow naturally from section to section
- Have an executive summary at the top
- Be written in a confident, professional tone
- Include a clear conclusion with next steps
- Be practical and actionable
- Be formatted with clear headings and sections"""
        ),
        (
            "human",
            """Please create a complete, professional Business Plan for:
**{business_idea}**

You have the following expert analyses to work with:

=== MARKET RESEARCH ===
{market_research}

=== COMPETITOR ANALYSIS ===
{competitor_analysis}

=== FINANCIAL PLAN ===
{financial_plan}

=== RISK ANALYSIS ===
{risk_analysis}

=== MARKETING STRATEGY ===
{marketing_strategy}

Please synthesize all of the above into one cohesive business plan with:
1. Executive Summary (2-3 paragraphs)
2. Business Overview
3. Market Opportunity (from market research)
4. Competitive Landscape (from competitor analysis)
5. Financial Projections (from financial plan)
6. Risk Management (from risk analysis)
7. Go-to-Market Strategy (from marketing strategy)
8. Conclusion & Recommended Next Steps (5 immediate action items)

Make it read like a professional document, not a list of separate reports."""
        )
    ])

    chain = prompt | llm | output_parser

    final_report = chain.invoke({
        "business_idea": business_idea,
        "market_research": market_research,
        "competitor_analysis": competitor_analysis,
        "financial_plan": financial_plan,
        "risk_analysis": risk_analysis,
        "marketing_strategy": marketing_strategy,
    })

    print("✅ Final business plan ready!")
    return final_report
