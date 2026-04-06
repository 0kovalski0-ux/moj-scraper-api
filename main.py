from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "API za filmove je aktivan! Koristi /stream ili /search."

@app.route('/stream')
def get_stream():
    tmdb_id = request.args.get('id')
    media_type = request.args.get('type', 'movie')

    if not tmdb_id:
        return jsonify({"error": "Missing ID"}), 400

    # ISPRAVLJEN LINK: dodat /embed/ i kosa crta pre media_type
    video_url = f"https://vidsrc.to{media_type}/{tmdb_id}"
    
    return jsonify({
        "url": video_url,
        "referer": "https://vidsrc.to"
    })

@app.route('/search')
def search_movies():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing query"}), 400
    
    # Ovo je test odgovor dok ne ubaciš TMDB ključ
    return jsonify({
        "results": [
            {"title": "Avatar", "id": "19995"},
            {"title": "Avatar: The Way of Water", "id": "76600"}
        ]
    })

# OVO MORA DA BUDE NA SAMOM KRAJU FAJLA
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

