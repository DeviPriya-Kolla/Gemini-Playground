import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv # Import load_dotenv

# Load environment variables from .env file
# This line should be at the very beginning of your script
load_dotenv()

# ==========================# App Configuration# ==========================
APP_TITLE = "✨ Gemini Chatbot"
APP_DESCRIPTION = (
    "Talk with a conversational AI powered by Google's **Gemini-1.5-Flash** model. "
    "This chatbot maintains conversation history for more natural interactions."
)

# ==========================# Model and API Setup# ==========================
try:
    # Get the API key from environment variables (loaded from .env or system)
    api_key = os.getenv("GOOGLE_API_KEY") # Use os.getenv() for consistency with dotenv

    if not api_key:
        raise ValueError(
            "❌ GOOGLE_API_KEY environment variable not found! "
            "Please set it in your system environment or create a .env file "
            "in the same directory as app.py with GOOGLE_API_KEY=YOUR_API_KEY_HERE"
        )

    # Configure the generative AI library
    genai.configure(api_key=api_key)

    # Initialize the Gemini model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="You are a friendly and helpful chatbot.",
        safety_settings={
            'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_NONE',
            'HARM_CATEGORY_HARASSMENT': 'BLOCK_NONE',
            'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_NONE',
            'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_NONE'
        }
    )
    MODEL_LOADED = True
    print("✅ Model loaded successfully.")

except Exception as e:
    # Print a more informative error message for debugging
    print(f"🔴 Error loading model: {e}")
    MODEL_LOADED = False

# ==========================# Chatbot Response Function (Stateless)# ==========================
def respond(message, history):
    """
    Generates a response from the Gemini model in a stateless manner.
    """
    if not MODEL_LOADED:
        yield "🔴 Error: The AI model could not be loaded. Please check the API key and restart the application."
        return # Stop execution if model isn't loaded

    try:
        # Convert Gradio's history format to the format Google's API expects
        google_history = []
        for user_msg, model_msg in history:
            google_history.append({"role": "user", "parts": [user_msg]})
            google_history.append({"role": "model", "parts": [model_msg]})

        # The user's new message is the last part of the history
        google_history.append({"role": "user", "parts": [message]})

        # Use the stateless generate_content method for streaming
        response = model.generate_content(google_history, stream=True)

        # Stream the response back to the UI
        full_response = ""
        for chunk in response:
            # Ensure the chunk has content before appending
            if chunk.text:
                full_response += chunk.text
                yield full_response
    except Exception as e:
        yield f"❌ An error occurred: {e}"

# ==========================# Gradio UI Setup# ==========================
demo = gr.ChatInterface(
    fn=respond,
    chatbot=gr.Chatbot(
        height=600,
        label="💬 Gemini Chatbot"
    ),
    textbox=gr.Textbox(
        placeholder="Type your message here...",
        container=False,
        scale=7
    ),
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    theme="soft",
    examples=[
        "What are some fun things to do in St. Louis, Missouri?",
        "Write a short, funny poem about a robot who loves to cook.",
        "Explain the concept of zero-shot learning in simple terms.",
    ],
    cache_examples=False,
)

# ==========================# Run the App# ==========================
if __name__ == "__main__":
    demo.launch()
