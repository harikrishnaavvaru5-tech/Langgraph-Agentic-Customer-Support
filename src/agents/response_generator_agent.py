import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))


from services.llm_services import call_gemini as model
from src.AgentState import AgentState


class ResponseGeneratorAgent:

    def __init__(self):
        self.model = model

    # ============ RESPONSE GENERATOR NODE ============
    def generate_response(self, state: AgentState) -> AgentState:

        """Generate final response based on inputs"""
    
        
        response_context = (
            f"Query: {state['customer_query']}\n"
            f"Intent: {state['intent']}\n"
            f"Agent Responses: {state['agent_responses']}\n"
            f"Human Feedback: {state.get('human_feedback', 'N/A')}"
        )

        prompt = (
            "Using the following context, generate a coherent and helpful response to the customer query.\n\n"
            f"{response_context}\n\n"
            "Final Response:"
        )

        response = model(prompt=prompt, model="gemini-2.5-flash")
        print("Final Response Generated:", response.text)
        state["final_response"] = response.text

        return state