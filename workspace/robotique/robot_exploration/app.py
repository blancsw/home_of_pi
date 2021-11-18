#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading

from cv2 import cv2
from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO, emit
import time

# from home_pi.motor_hat import MotorDriver
from home_pi.camera_stream import CameraStream

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
lock = threading.Lock()
socketio = SocketIO(app, async_mode=async_mode)
camera = CameraStream()


def generate():
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            frame = camera.get_frame()
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if frame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", frame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
        time.sleep(0.2)
        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(), mimetype="multipart/x-mixed-replace; boundary=frame")


@socketio.event
def up_event():
    print("up_event")


@socketio.event
def down_event():
    print("down_event")


@socketio.event
def left_event():
    print("left_event")


@socketio.event
def right_event():
    print("right_event")


@socketio.event
def stop_move():
    print("stop_event")


@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def connect():
    print('Client connected', request.sid)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)


if __name__ == '__main__':
    socketio.run(app)
