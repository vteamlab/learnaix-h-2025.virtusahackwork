from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import get_gpt_response, log_query

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can call backend

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    reply = get_gpt_response(user_input)
    log_query(user_input, reply)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
