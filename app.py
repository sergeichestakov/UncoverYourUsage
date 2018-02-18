from flask import Flask, request, send_from_directory, jsonify
import os
import pandas as pd
import numpy as np
import csv

from model.model import EnergyModel

app = Flask(__name__, static_url_path='/client')
model = EnergyModel()
model.output()
@app.route('/')
def home():
    print(os.path.join(app.root_path, 'client'))
    return send_from_directory(os.path.join(app.root_path, 'client'), 'index.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(os.path.join(app.root_path, 'client'), path)

@app.route('/predict', methods=['POST'])
def predict():
    print("Predicting household energy usage!")
    req = request.get_json(force=True)
    file = open("dump.csv", "w")
    writer = csv.writer(file)
    writer.writerow([
    'TOTCSQFT',
    'ACROOMS',
    'BEDROOMS',
    'WASHLOAD',
    'USECENAC',
    'NCOMBATH',
    'TYPEHUQ',
    'TEMPHOME',
    'CENACHP',
    'TEMPNITEAC',
    'SWIMPOOL',
    'NUMCFAN',
    'MAINTAC',
    'COOLTYPE',
    ])
    writer.writerow(req)
    file.close()
    csver = open("dump.csv", "r")
    parameters = pd.read_csv(csver)
    answer = model.predict(parameters)
    return jsonify(answer)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
