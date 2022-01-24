from flask import Flask, jsonify
import json
app = Flask(__name__)

@app.route('/')
def index():
  return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

app.run(host = '0.0.0.0', port = 5000)