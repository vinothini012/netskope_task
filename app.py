import sqlite3
import subprocess
from flask import Flask, request
import pickle

app = Flask(__name__)

# Vulnerability 1: SQL Injection (CWE-89)
@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # This query is vulnerable to SQL Injection
    query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    return "User created successfully"

# Vulnerability 2: Command Injection (CWE-78)
@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')
    # This command is vulnerable to Command Injection
    result = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True)
    return result.stdout

# Vulnerability 3: Insecure Deserialization (CWE-502)
@app.route('/load_user', methods=['POST'])
def load_user():
    data = request.form['data']
    # This line is vulnerable to Insecure Deserialization
    user = pickle.loads(data)
    return f"Loaded user: {user}"

if __name__ == '__main__':
    app.run(debug=True)

