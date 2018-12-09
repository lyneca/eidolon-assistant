from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/assistant', methods=['POST'])
def assistant():
    json = request.get_json()
    text = json['queryResult']['queryText']
    if "hello there" in text.lower():
        return jsonify({
            "fulfillmentText": "General Kenobi! You are a bold one!"
            })
    elif "eidolon" in text.lower():
        return jsonify({
            "fulfillmentText": "I'm not 100% sure, sorry."
            })

if __name__ == '__main__':
    app.run()
