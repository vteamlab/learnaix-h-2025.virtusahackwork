# learnaix-h-2025.virtusahackwork
📘 LearnAIx AI Companion (Local Prototype)

This project is a local AI Companion prototype for the LearnAIx platform. It uses OpenAI GPT to provide learners with navigation help, query resolution, doubt clarification, multilingual support, and soft-skills enhancement.

The setup is standalone (no Moodle/Snowflake required) so you can test and demo the AI Companion immediately.

🚀 Features

Chat interface powered by OpenAI GPT (gpt-4-mini).

Real-time learner support for queries.

Multilingual responses (English, Spanish, etc.).

Logs all conversations in chat_log.txt.

Ready for integration into Moodle or LearnAIx beta.

📂 Project Structure
ai_companion_local/
│
├── backend/
│   ├── app.py          # Flask backend server
│   ├── config.py       # OpenAI API key & model config
│   └── utils.py        # GPT response + logging
│
├── frontend/
│   ├── index.html      # Chat UI
│   ├── script.js       # Calls backend API
│   └── style.css       # Styling (optional)
│
└── requirements.txt    # Python dependencies

🛠️ Setup Instructions
1. Clone the project
git clone <your-repo-url>
cd ai_companion_local

2. Install dependencies
pip install -r requirements.txt

3. Configure your API key

Edit backend/config.py:

OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MODEL_NAME = "gpt-4-mini"


👉 Get your key from: OpenAI API Keys

4. Start the backend
cd backend
python app.py


Backend runs at: http://127.0.0.1:5000

5. Start the frontend

In a new terminal:

cd frontend
python -m http.server 8000


Open in browser: http://localhost:8000

🧪 Testing the Chat

In the chat box, try questions like:

Navigation help:
How do I find my pending assignments?

Soft skills guidance:
How can I improve my teamwork communication skills?

Doubt clarification:
Explain machine learning overfitting in simple terms.

Multilingual query:
Por favor, dame consejos para mejorar mis habilidades de estudio.

Learning suggestions:
Suggest a learning path to improve Python and SQL.

✅ All queries and replies are logged in backend/chat_log.txt.

⚠️ Troubleshooting

401 Unauthorized / Invalid API key → Ensure your API key is valid in config.py.

CORS error → Always open frontend via local server (http://localhost:8000), not by double-clicking index.html.

No response → Confirm Flask is running (http://127.0.0.1:5000) and check browser console (F12 → Console).
