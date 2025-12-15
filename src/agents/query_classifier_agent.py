import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))


# This is like a router agent that classifies customer queries into categories like FAQ, Technical, Billing, etc.
import json
from services import llm_services as model
from src.AgentState import AgentState

class QueryClassifierAgent:

    def __init__(self):

        self.model = model

    def classify_query(self, state: AgentState) -> AgentState:

        """This is a Query Classifier Agent function that classifies the intent and urgency of a customer query."""

        prompt = f"""Analyze this customer support query:
        {state['customer_query']}
        
        Classify:
        1. Intent (FAQ, Technical, Billing, Other)
        2. Urgency (low/medium/high)
        3. Confidence (0.0-1.0)
        
        Respond in JSON format:
        {{"intent": "...", "urgency": "...", "confidence": ...}}"""
        
        response = self.model.call_gemini(prompt, model="gemini-2.5-flash")

        response_text = response.candidates[0].content.parts[0].text
        
        # Remove markdown code block formatting if present
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
            response_text = response_text.strip()
    
        result = json.loads(response_text)
        
        state.update({
            "intent": result["intent"],
            "urgency_level": result["urgency"],
            "confidence_score": result["confidence"]
        })

        return state