from flask import Flask, jsonify, send_from_directory, request
import os
import requests
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()  # this reads from .env

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})

@app.route("/api/key")
def get_key():
    return jsonify({"apiKey": os.getenv("NYT_API_KEY")})

@app.route("/api/local-news")
def get_local_news():
    api_key = os.getenv("NYT_API_KEY")
    if not api_key:
        return jsonify({"error": "API key not found"}), 500

    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "q": "Sacramento (Calif) OR Davis (Calif)",
        "api-key": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
@app.route("/<path:path>")
def serve_frontend(path=""):
    if path != "" and os.path.exists(f"static/{path}"):
        return send_from_directory("static", path)
    return send_from_directory("templates", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
