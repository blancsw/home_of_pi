#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from collections import deque
from queue import Queue
from threading import Thread

import cv2


class KeyClipWriter:
    def __init__(self, bufSize=64, timeout=1.0):
        # store the maximum buffer size of frames to be kept
        # in memory along with the sleep timeout during threading
        self.bufSize = bufSize
        self.timeout = timeout

        # initialize the buffer of frames, queue of frames that
        # need to be written to file, video writer, writer thread,
        # and boolean indicating whether recording has started or not
        self.Q = None
        self.writer = None
        self.thread = None
        self.recording = False

    def update(self, frame):
        # if we are recording, update the queue as well
        if self.recording:
            self.Q.put(frame)

    def start(self, frame, outputPath, fourcc, fps):
        print("Start recording")
        # indicate that we are recording, start the video writer,
        # and initialize the queue of frames that need to be written
        # to the video file
        self.recording = True
        self.writer = cv2.VideoWriter(outputPath, fourcc, fps,
                                      (frame.shape[1], frame.shape[0]), True)
        self.Q = Queue()
        self.update(frame)

        # start a thread write frames to the video file
        self.thread = Thread(target=self.write, args=())
        self.thread.daemon = True
        self.thread.start()

    def write(self):
        # keep looping
        while True:
            # if we are done recording, exit the thread
            if not self.recording:
                return

            # check to see if there are entries in the queue
            if not self.Q.empty():
                # grab the next frame in the queue and write it
                # to the video file
                frame = self.Q.get()
                self.writer.write(frame)

            # otherwise, the queue is empty, so sleep for a bit
            # so we don't waste CPU cycles
            else:
                time.sleep(self.timeout)

    def flush(self):
        # empty the queue by flushing all remaining frames to file
        while not self.Q.empty():
            frame = self.Q.get()
            self.writer.write(frame)

    def finish(self):
        print("Stop recording")
        # indicate that we are done recording, join the thread,
        # flush all remaining frames in the queue to file, and
        # release the writer pointer
        self.recording = False
        if self.thread is not None:
            self.thread.join()
        self.flush()
        self.writer.release()
