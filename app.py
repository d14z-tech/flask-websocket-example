from flask import Flask, render_template
from flask_socketio import SocketIO
import base64
from PIL import Image
import io

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# here check the connection to the client
@socketio.on('connect')
def handle_connect():
    print('Client connected')

# here listen to a message event
@socketio.on('message')
def handle_message(data):
    base64_string = ""

    # here decode the base64 image
    if "data:image" in data:
        base64_string = data.split(",")[1]

    image_bytes = base64.b64decode(base64_string)
    # here is the image of the video to do anything what you want like send it to a model
    img = Image.open(io.BytesIO(image_bytes))

    # here go the response
    response = { 'something': 'anything' }
    socketio.emit('response', response) # here emit the response

    print('received message: ok')

# Other event handlers go here

if __name__ == '__main__':
    socketio.run(app, debug=True)
