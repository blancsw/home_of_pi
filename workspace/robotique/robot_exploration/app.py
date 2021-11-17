#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Lock

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
# from home_pi.motor_hat import MotorDriver


async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


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
