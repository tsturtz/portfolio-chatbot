from flask import Flask, request, jsonify
from src.resources import load_website_docs, split_documents, create_vectorstore
from src.tools import make_retriever_tool
from src.agent import create_agent_executor


app = Flask(__name__)

# Load and split website content
docs = load_website_docs(["https://taylorsturtz.com"])
split_docs = split_documents(docs)
print(f"Split into {len(split_docs)} chunks.")

# Create vector embeddings and store them in Chroma DB
vectorstore = create_vectorstore(split_docs)
print("Chroma vectorstore created.")
retriever = vectorstore.as_retriever()

# Tool + agent setup
retrieve_documents_tool = make_retriever_tool(retriever)
agent_executor = create_agent_executor([retrieve_documents_tool])

# Flask routes
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