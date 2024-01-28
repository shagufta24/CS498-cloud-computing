from flask import Flask, jsonify
import socket, subprocess, os
app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(current_folder, 'stress_cpu.py')
    process = subprocess.Popen(['python3', script_path])
    return jsonify({'message': 'Subprocess launched'}), 200
    
@app.route('/', methods=['GET'])
def get_host():
    return socket.gethostname(), 200

if __name__ == '__main__':
   app.run(host="0.0.0.0")