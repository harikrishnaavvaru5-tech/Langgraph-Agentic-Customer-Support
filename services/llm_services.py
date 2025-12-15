import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def call_gemini(
    prompt: str,
    model: str = "gemini-2.5-flash",
    temperature: float = 0.7,
    max_tokens: int = 1024
) -> str:
    
    """
    Call Google Gemini API with the provided prompt.
    
    Args:
        prompt: The input text prompt
        model: The model to use (default: gemini-2.5-flash)
        temperature: Sampling temperature (0.0-2.0, default: 0.7)
                     Lower values = more deterministic, higher = more creative
        max_tokens: Maximum number of tokens in response (default: 1024)
    
    Returns:
        The generated text response
    """
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model_instance = genai.GenerativeModel(model)
    
    response = model_instance.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens
        )
    )

    return response






# Example usage

'''
GenerativeModel
Use genai.GenerativeModel to access the API:

    import google.generativeai as genai
    import os

    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel(model_name='gemini-2.5-flash')
    response = model.generate_content('Teach me about how an LLM works')

    print(response.text)'''