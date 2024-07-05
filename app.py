import sqlite3
import subprocess
from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: SQL Injection (CWE-89)
def create_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(query)
    conn.commit()
    conn.close()

# Vulnerability 2: Command Injection (CWE-78)
@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')
    result = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True)
    return result.stdout

# Vulnerability 3: Cross-Site Scripting (XSS) (CWE-79)
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return f"<h1>Hello, {name}!</h1>"

# Vulnerability 4: Insecure Deserialization (CWE-502)
import pickle

def load_user(data):
    user = pickle.loads(data)
    return user

if __name__ == '__main__':
    app.run(debug=True)

