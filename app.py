from flask import Flask, request
import requests
from markupsafe import escape

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f'<h1>Hello, {name}

if __name__ == '__main__':
    app.run(debug=True)
