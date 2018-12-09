from flask import Flask, request

app = Flask(__name__)

@app.route('/assistant', methods=['POST'])
def assistant():
    print(request.get_json())
    return ""

if __name__ == '__main__':
    app.run()
