from flask import Flask, request, render_template, jsonify
from scanner.scanner import Scanner
from scanner.payload_manager import PayloadManager
import os

app = Flask(__name__)
payload_manager = PayloadManager("payloads/")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    url = data['url']
    params = data.get('params', [])
    payloads = data.get('payloads', [])

    scanner = Scanner(url, params, payload_manager)
    results = scanner.run_scan()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)