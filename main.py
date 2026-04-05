from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ovo pokriva glavni link: http://192.168.0
@app.route('/')
def home():
    return jsonify({
        "status": "Server je online",
        "poruka": "Koristi /stream za link"
    })

# Ovo pokriva link: http://192.168.0stream
@app.route('/stream')
def get_stream():
    # Link koji si izvukao iz curl komande
    direct_url = "https://plexvideos.com"
    
    return jsonify({
        "url": direct_url,
        "referer": "https://plex.tv"
    })

if __name__ == '__main__':
    # host='0.0.0.0' omogućava telefonu da vidi server na tvojoj mreži
    app.run(host='0.0.0.0', port=5000, debug=True)
