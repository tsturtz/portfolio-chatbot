from flask import Flask, request, jsonify

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

# Flask routes
@app.route("/", methods=["GET"])
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                background-color: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .welcome-box {
                background-color: #ffffff;
                padding: 2.5rem 4rem;
                border-radius: 12px;
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
                text-align: center;
                border: 1px solid #e2e8f0;
            }
            h1 {
                color: #2d3748;
                font-size: 2.5rem;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="welcome-box">
            <h1>Hello, Agent is Ready!</h1>
        </div>
    </body>
    </html>
    """

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "up"})

@app.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json(force=True)
    prompt_text = data.get("prompt", "")
    if not prompt_text:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        result = agent_executor.invoke({"input": prompt_text})
        return jsonify({"response": result.get("output")})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)