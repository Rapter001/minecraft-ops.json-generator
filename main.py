from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    name = request.form['name']
    level = int(request.form['level'])
    bypass = request.form.get('bypass') == 'on'

    # Fetch UUID from Mojang API
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    if response.status_code != 200:
        return jsonify({"error": "Invalid username or UUID not found."}), 400

    uuid = response.json()['id']

    ops_data = [{
        "uuid": uuid,
        "name": name,
        "level": level,
        "bypassesPlayerLimit": bypass
    }]

    return jsonify(ops_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=False)