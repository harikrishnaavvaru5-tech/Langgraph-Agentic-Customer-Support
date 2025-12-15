import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))


from services.llm_services import call_gemini as model
from src.AgentState import AgentState


class FAQAgent:

    def __init__(self):

        self.model = model


    def faq_agent(self, state: AgentState) -> AgentState:

        """FAQ Agent to handle frequently asked questions from customers"""
    
        # prompt = f"""You are an expert customer support agent. Provide a concise and accurate answer to the following FAQ:
        # {state['customer_query']}"""

        # response = self.model(prompt, model="gemini-2.5-flash")

        response = "Please reset your password by clicking on 'Forgot Password' at the login page."
        
        state["agent_responses"]["faq"] = response
        
        return state