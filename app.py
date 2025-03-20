from flask import Flask
import getpass
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')

def htop():
    full_name = "RAHUL Y S"
    username = getpass.getuser()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    return f"<h1>System Information</h1><p><strong>Name:</strong> {full_name}</p><p><strong>Username:</strong> {username}</p><p><strong>Server Time (IST):</strong> {server_time}</p><pre>{top_output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
