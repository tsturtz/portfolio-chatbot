from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from src.tools import make_tools
from src.agent import create_agent_executor
from src.db.connect import connect_to_vectorstore

app = Flask(__name__)

# Connect to Chroma Cloud
vectorstore = connect_to_vectorstore()

# Tool + agent setup
retriever = vectorstore.as_retriever()
tools = make_tools(retriever)
agent_executor = create_agent_executor(tools)

# Flask-Limiter to rate limit requests based on the user's IP address
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["100 per day", "50 per hour", "10 per minute"]
)

# Flask routes
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "up"})

@app.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json(force=True)
    prompt_text = data.get("prompt", "")
    if not prompt_text:
        return jsonify({"error": "No prompt provided"}), 400
    if len(prompt_text) > 500:
        return jsonify({"error": "Prompt too long"}), 400

    try:
        result = agent_executor.invoke({"input": prompt_text})
        return jsonify({"response": result.get("output")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)