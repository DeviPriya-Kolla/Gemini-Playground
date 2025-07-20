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

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

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


![Gemini Chatbot Demo](/Gemini%20Chatbot%20Interface.png)

<!-- For Hugging Face README only: -->
<!-- <iframe src="https://huggingface.co/spaces/DeviPriyaK/Gemini-Playground?embed=true" width="850" height="450"></iframe> -->