import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# OVDE STAVI SVOJ KLJUČ SA TMDB SAJTA
TMDB_API_KEY = "5d377e052d891d6518d185f610d6b8e8"

@app.route('/search')
def search_movies():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing query"}), 400
    
    # PRAVA PRETRAGA PREKO TMDB-A
    url = f"https://themoviedb.org{TMDB_API_KEY}&query={query}"
    response = requests.get(url).json()
    
    return jsonify(response)

@app.route('/stream')
def get_stream():
    tmdb_id = request.args.get('id')
    media_type = request.args.get('type', 'movie')
    video_url = f"https://vidsrc.to{media_type}/{tmdb_id}"
    return jsonify({"url": video_url})

if __name__ == '__main__':
    app.run()
