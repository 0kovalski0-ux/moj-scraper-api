from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/stream')
def get_stream():
    # Uzimamo ID koji šalje Flutter (npr. 550)
    tmdb_id = request.args.get('id')
    media_type = request.args.get('type', 'movie')

    if not tmdb_id:
        return jsonify({"error": "Missing ID"}), 400

    # Koristimo stabilan izvor koji ne ističe kao Plex
    # Ovo je "pametan" link koji HDO Box i slični koriste
    video_url = f"https://vidsrc.to{media_type}/{tmdb_id}"
    
    return jsonify({
        "url": video_url,
        "referer": "https://vidsrc.to"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
@app.route('/search')
def search_movies():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing query"}), 400
    
    # Ovde koristimo TMDB API (trebaće ti tvoj API KEY ako hoćeš prave rezultate)
    # Za početak, evo kako da vratiš bar neki odgovor da Render ne "vrti"
    return jsonify({
        "results": [
            {"title": "Avatar", "id": "19995"},
            {"title": "Avatar: The Way of Water", "id": "76600"}
        ]
    })
