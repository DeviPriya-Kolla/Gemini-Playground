## 📝 About

**Gemini Chatbot** is an interactive conversational AI application built with [Gradio](https://gradio.app/) that leverages the power of Google's Gemini API. It provides users with a simple chat interface to interact with the chatbot, which responds intelligently using Google’s language models. This project demonstrates how to integrate external APIs into a Python web app and deploy it seamlessly on Hugging Face Spaces.

- **Tech Stack:** Python, Gradio, Google Gemini API
- **Features:** Real-time chat, easy deployment, customizable interface
- **Use Cases:** Demos, learning, prototyping conversational AI

---
title: Gemini Chatbot
emoji: ⚡
colorFrom: yellow
colorTo: gray
sdk: gradio
sdk_version: 5.35.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Chatbot which uses Google API
---

🚀 [Try the Gemini Chatbot on Hugging Face Spaces](https://huggingface.co/spaces/DeviPriyaK/Gemini-Playground)

---

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DeviPriya-Kolla/Gemini-Playground.git
   cd Gemini-Playground
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google API key:**
   - Create a `.env` file or set the environment variable as required by your app.

4. **Run the app:**
   ```bash
   python app.py
   ```
   or, if using Gradio CLI:
   ```bash
   gradio app.py
   ```
5. **How to push to both remotes:**
   ```bash
   git push origin main      # For Hugging Face
   git push github main      # For GitHub
   ```
---

## 📝 Working Instructions

- Enter your message in the chat interface.
- The chatbot will respond using the Google API.
- For any configuration, check the `app.py` file and update as needed.

---

## Demo Screenshot
![Gemini Chatbot Demo](/Gemini%20Chatbot%20Interface.png)

<!-- For Hugging Face README only: -->
<!-- <iframe src="https://huggingface.co/spaces/DeviPriyaK/Gemini-Playground?embed=true" width="850" height="450"></iframe> -->