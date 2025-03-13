import google.generativeai as genai

MODEL_NAME = "gemini-1.5-pro-latest"  # Or another available model

genai.configure(api_key="AIzaSyCJfR9nmn4OlHgqMZw8fvm2XLd1t8B6BBQ")

def ask_gemini(user_input):
    model = genai.GenerativeModel(MODEL_NAME)
    
    # Add system instruction to keep responses focused on insurance
    prompt = f"""You are BiBi, an insurance assistant. Answer only insurance-related questions. 
    If the question is unrelated to insurance, politely redirect the user to ask about insurance.
    
    User's question: {user_input}
    """
    
    response = model.generate_content(prompt)  # Sends structured input to the model
    return response.text  # Extracts the response text

# Example usage
user_input = "Tell me about your savings plan."
response = ask_gemini(user_input)
print(response)
