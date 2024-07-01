from flask import Flask, request
import requests
from markupsafe import escape

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    if url:
        response = requests.get(url)
        return response.content
    return 'Please provide a URL parameter.'

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f'<h1>Hello, {escape(name)}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)