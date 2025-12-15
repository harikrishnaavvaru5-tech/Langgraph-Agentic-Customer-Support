import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from langgraph.graph import StateGraph, START, END
from src.AgentState import AgentState
from src.agents.query_classifier_agent import QueryClassifierAgent
from src.agents.faq_agent import FAQAgent
from src.agents.technical_agent import TechnicalAgent
from src.agents.billing_agent import BillingAgent
from src.agents.escalation_agent import EscalationAgent
from src.agents.human_review_agent import HumanReviewAgent
from src.agents.response_generator_agent import ResponseGeneratorAgent


def build_support_graph() -> StateGraph:
    """Build the LangGraph workflow"""
    graph = StateGraph(AgentState)
    
    # Initialize agent instances
    classifier = QueryClassifierAgent()
    faq = FAQAgent()
    technical = TechnicalAgent()
    billing = BillingAgent()
    escalation = EscalationAgent()
    human_review = HumanReviewAgent()
    response_gen = ResponseGeneratorAgent()
    
    # Add nodes - pass method references, don't call them
    graph.add_node("classifier", classifier.classify_query)
    graph.add_node("faq_agent", faq.faq_agent)
    graph.add_node("technical_agent", technical.technical_agent)
    graph.add_node("billing_agent", billing.billing_agent)
    graph.add_node("escalation_decision", escalation.escalation_decision)
    graph.add_node("human_review", human_review.human_review)
    graph.add_node("response_generator", response_gen.generate_response)
    
    # Add edges
    graph.add_edge(START, "classifier")
    
    # Routing based on intent
    graph.add_conditional_edges(
        "classifier",
        lambda state: state["intent"],
        {
            "FAQ": "faq_agent",
            "Technical": "technical_agent",
            "Billing": "billing_agent",
            "Other": "faq_agent"
        }
    )
    
    # All agents → escalation decision
    for agent in ["faq_agent", "technical_agent", "billing_agent"]:
        graph.add_edge(agent, "escalation_decision")
    
    graph.add_edge("escalation_decision", "human_review")
    graph.add_edge("human_review", "response_generator")
    graph.add_edge("response_generator", END)
    
    return graph.compile()


class Orchestrator:
    """Orchestrator to build and manage the support workflow graph"""

    def __init__(self):
        self.state = AgentState()


# ============ MAIN EXECUTION ============
if __name__ == "__main__":
    # Initialize support workflow
    support_app = build_support_graph()
    
    # Example query
    initial_state = {
        "customer_query": "My account is locked, I can't log in",
        "intent": "",
        "urgency_level": "",
        "confidence_score": 0.0,
        "agent_responses": {},
        "human_escalation_required": False,
        "human_feedback": "",
        "final_response": "",
        "conversation_history": []
    }
    
    # Execute workflow
    result = support_app.invoke(initial_state)
    print("\n✅ Final Response:")
    print(result["final_response"])