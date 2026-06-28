from flask import Flask, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')

@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

if __name__ == '__main__':
    # Сайт очилади: http://127.0.0.1:5000
    app.run(debug=True, port=5000)
