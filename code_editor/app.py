from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)
# Initialize code content and user data
code_content = ""
users = {}
@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('A user connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('A user disconnected')

@socketio.on('update_code')
def handle_update_code(data):
    global code_content
    code_content = data['code']
    emit('code_updated', {'code': code_content}, broadcast=True)
    
@socketio.on('execute_code')
def handle_execute_code(data):
    code = data['code']
    print("Received code:", code)  # Add this line for debugging
    try:
        # Execute the code and capture the output
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError as e:
        # Handle errors
        result = e.output
    emit('code_executed', {'output': result})
if __name__ == '__main__':
    socketio.run(app, debug=True)
