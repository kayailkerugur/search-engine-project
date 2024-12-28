from flask import Blueprint, request, jsonify
from app.services import search_google, search_bing, search_gpt

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return {"message": "Hello, Search Engine!"}

@main_bp.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    print(query)
    google_results = search_google(query)
    #bing_results = search_bing(query)
    #gpt_results = search_gpt(query)
    combined_results = {
        "query": query,
        "google": google_results.get("items", []),
        "bing": "bing_results.get(""webPages"", {}).get(""value"", [])",
        "gpt": "gpt_results.strip()"
    }

    return jsonify(combined_results)
