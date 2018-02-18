from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_url_path='/client')

@app.route('/')
def home():
    print(os.path.join(app.root_path, 'client'))
    return send_from_directory(os.path.join(app.root_path, 'client'), 'index.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(os.path.join(app.root_path, 'client'), path)

@app.route('/predict', methods=['POST'])
def process():
    print("Predicting household energy usage!")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
