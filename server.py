from flask import Flask

app = Flask(__name__)

@app.route('assistant', methods=['POST'])
def assistant():
    print(request.get_json())
    return ""

if __name__ == '__main__':
    app.run()
