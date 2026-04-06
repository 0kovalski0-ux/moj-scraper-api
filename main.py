import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TMDB_API_KEY = "5d377e052d891d6518d185f610d6b8e8"
TMDB_BASE = "https://api.themoviedb.org/3"

@app.route('/')
def home():
    return {"status": "OK", "message": "API radi"}

# ================= SEARCH =================
@app.route('/search')
def search_movies():
    query = request.args.get('q')

    if not query:
        return jsonify({"error": "Missing query"}), 400

    url = f"{TMDB_BASE}/search/movie?api_key={TMDB_API_KEY}&query={query}"

    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ================= STREAM =================
@app.route('/stream')
def get_stream():
    tmdb_id = request.args.get('id')
    media_type = request.args.get('type', 'movie')

    if not tmdb_id:
        return jsonify({"error": "Missing ID"}), 400

    # vidsrc embed format
    video_url = f"https://vidsrc.to/embed/{media_type}/{tmdb_id}"

    return jsonify({
        "url": video_url
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
