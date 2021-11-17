#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import time

import cv2
import imutils
import numpy as np
from imutils.video import VideoStream

from .conf import Conf
from .keyclipwriter import KeyClipWriter


class MotionDetection:
    GREEN_COLOR = (0, 255, 0)

    def __init__(self, conf_path: str):
        """

        Args:
            conf_path:
        """
        # load the configuration file
        self.conf = Conf(conf_path)
        # initialize key clip writer and the consecutive number of
        # frames that have *not* contained any action
        self.kcw = KeyClipWriter(bufSize=self.conf["buffer_size"])
        self.consec_frames = 0

        # initialize the MOG foreground background subtractor
        self.fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(
            history=self.conf["mog_history"],
            nmixtures=self.conf["mog_nmixtures"],
            backgroundRatio=self.conf["mog_bg_ratio"],
            noiseSigma=self.conf["mog_noise_sigma"])

        # create erosion and dilation kernels
        self.eKernel = np.ones((7, 7), np.uint8)
        self.dKernel = np.ones((3, 3), np.uint8)
        self.update_consec_frames = True

        self.video_stream = VideoStream(usePiCamera=self.conf["picamera"]).start()
        time.sleep(2.0)

    def get_frame(self):
        """

        Returns:

        """
        # grab the current frame, resize it, and initialize a
        # boolean used to indicate if the consecutive frames
        # counter should be updated
        frame = self.video_stream.read()
        frame = imutils.resize(frame, width=self.conf["resize"])

        # flag to update the counter consecutive frames with no motion
        self.update_consec_frames = True

        # apply forground background subtraction with the
        # GMG algorithm
        mask = self.fgbg.apply(frame)

        # erode the mask to eliminate noise and then
        # dilate the mask to fill in holes
        mask = cv2.erode(mask, self.eKernel, iterations=3)
        mask = cv2.dilate(mask, self.dKernel, iterations=2)

        # find contours
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            # find the largest contour in the mask, then use it
            # to compute the minimum enclosing circle
            c = max(cnts, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(c)
            self.update_consec_frames = (w * h) <= self.conf["min_area"]
            if self.update_consec_frames:
                self.start_recording(frame)
                self.consec_frames = 0
                return True, {
                    "frame": frame,
                    "x": x,
                    "y": y,
                    "width": w,
                    "height": h
                }
        return False, {}

    def save_frame(self, frame):
        """

        Args:
            frame:

        Returns:

        """
        # otherwise, no action has taken place in this frame, so
        # increment the number of consecutive frames that contain
        # no action
        if self.update_consec_frames:
            self.consec_frames += 1

        # update the key frame clip buffer
        self.kcw.update(frame)

        # if we are recording and reached a threshold on consecutive
        # number of frames with no action, stop recording the clip
        if self.kcw.recording and self.consec_frames == self.conf["buffer_size"]:
            self.kcw.finish()

    def is_recording(self):
        """

        Returns:

        """
        return self.kcw.recording

    def start_recording(self, frame):
        """

        Returns:

        """
        # if we are not already recording, start recording
        if not self.is_recording():
            timestamp = datetime.datetime.now()
            os.makedirs(self.conf["output_videos_path"], exist_ok=True)
            path = "{}/{}.avi".format(self.conf["output_videos_path"], timestamp.strftime("%Y%m%d-%H%M%S"))
            self.kcw.start(frame, path, cv2.VideoWriter_fourcc(*self.conf["codec"]), self.conf["output_fps"])

    def __del__(self):
        """

        Returns:

        """
        # show a message to the user
        print("[INFO] cleaning up...")

        # if we are in the middle of recording a clip, wrap it up
        if self.kcw.recording:
            self.kcw.finish()
        self.video_stream.stop()
