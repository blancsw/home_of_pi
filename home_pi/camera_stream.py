#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import imutils
from imutils.video import VideoStream

from .conf import Conf


class CameraStream:

    def __init__(self, conf_path: str):
        # load the configuration file
        self.conf = Conf(conf_path)
        self.video_stream = VideoStream(usePiCamera=self.conf["picamera"]).start()
        time.sleep(2.0)

    def get_frame(self):
        # grab the current frame, resize it, and initialize a
        # boolean used to indicate if the consecutive frames
        # counter should be updated
        frame = self.video_stream.read()
        return imutils.resize(frame, width=self.conf["resize"])

    def __del__(self):
        """

        Returns:

        """
        # show a message to the user
        print("[INFO] cleaning up...")
        self.video_stream.stop()
