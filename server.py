from flask import Flask, request, jsonify

app = Flask(__name__)

def send_text(string):
    return jsonify({"fulfillmentText": string})

@app.route('/assistant', methods=['POST'])
def assistant():
    json = request.get_json()
    text = json['queryResult']['queryText']
    print(json)
    if "hello there" in text.lower():
        return sendtext("General Kenobi! You are a bold one!")
    if "eidolon" in text.lower():
        return send_text("I'm not 100% sure, sorry.")
    return send_text("I'm sorry, not sure what you mean by that.")

if __name__ == '__main__':
    app.run()
