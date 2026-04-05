from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/stream')
def get_stream():
    # Uzimamo TMDB ID koji šalje tvoja aplikacija (npr. ?id=550)
    tmdb_id = request.args.get('id')
    
    if not tmdb_id:
        # Ako nema ID-ja, vraćamo onaj tvoj Plex test link da aplikacija ne pukne
        return jsonify({
            "url": "https://plexvideos.com",
            "referer": "https://plex.tv"
        })

    # PAMETNA LOGIKA: Pravimo link za Vidsrc na osnovu ID-ja
    # Vidsrc je "embed" plejer koji u sebi sadrži filmove
    vidsrc_url = f"https://vidsrc.to{tmdb_id}"
    
    return jsonify({
        "url": vidsrc_url,
        "referer": "https://vidsrc.to"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
