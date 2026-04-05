from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "status": "Server je online",
        "poruka": "Koristi /stream za link"
    })

@app.route('/stream')
def get_stream():
    # TVOJ NOVI SVEŽI LINK KOJI SI IZVUKAO
    direct_url = "https://vod-content.plexvideos.com/ad-server/69b4ae7be22040599208b5d2/16ee30c1-9e6e-421d-8ede-bb7aadbff84d/21ba66b2376329e2b1e2c697de0615cc.mp4"
    
    return jsonify({
        "url": direct_url,
        "referer": "https://plex.tv"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
