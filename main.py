import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# TVOJ KLJUČ JE ISPRAVAN
TMDB_API_KEY = "5d377e052d891d6518d185f610d6b8e8"

@app.route('/search')
def search_movies():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing query"}), 400
    
    # ISPRAVLJEN URL ZA TMDB
    url = f"https://themoviedb.org{TMDB_API_KEY}&query={query}"
    
    try:
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/stream')
def get_stream():
    tmdb_id = request.args.get('id')
    media_type = request.args.get('type', 'movie')

    if not tmdb_id:
        return jsonify({"error": "Missing ID"}), 400

    # ISPRAVLJEN URL ZA STRIM (mora /embed/ i kosa crta)
    video_url = f"https://vidsrc.to{media_type}/{tmdb_id}"
    
    return jsonify({
        "url": video_url,
        "referer": "https://vidsrc.to"
    })

if __name__ == '__main__':
    app.run()
