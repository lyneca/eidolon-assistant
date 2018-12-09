from flask import Flask, request, jsonify
import requests as req
from datetime import datetime

app = Flask(__name__)

def get_expiry(j):
    return [x for x in j['SyndicateMissions'] if x['Tag'] == 'CetusSyndicate'][0]['Expiry']['$date']['$numberLong']

def time_until(ts):
    return (datetime.fromtimestamp(ts/1000) - datetime.now()).seconds

def get_next_timestamp():
    j = req.get('http://content.warframe.com/dynamic/worldState.php').json()
    seconds = time_until(int(get_expiry(j)))
    return (seconds // 60, seconds % 60)

def send_text(string):
    return jsonify({"fulfillmentText": string})

def match_in_order(text, match):
    indexes = [text.lower().find(word) for word in match.lower().split(' ')]
    if all([i >= 0 for i in indexes]) and indexes == sorted(indexes):
        return True
    return False

@app.route('/assistant', methods=['POST'])
def assistant():
    json = request.get_json()
    text = json['queryResult']['queryText']
    if text == "GOOGLE_ASSISTANT_WELCOME":
        return send_text("Hello! What can I help you with?")
    if "hello there" in text.lower():
        return send_text("General Kenobi! You are a bold one!")
    if match_in_order(text, "how long until night"):
        minutes, seconds = get_next_timestamp()
        if minutes > 50:
            return send_text("It's {} minutes and {} seconds until night on the Plains.".format(minutes, seconds))
        else:
            return send_text("It's {} minutes and {} seconds until morning on the Plains.".format(minutes, seconds))
    return send_text("I'm sorry, not sure what you mean by that.")

if __name__ == '__main__':
    app.run()
