#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from imutils.video import VideoStream


class CameraStream:

    def __init__(self, camera_src: int = 0, usePiCamera: bool = False, resolution=(320, 240)):
        self.video_stream = VideoStream(src=camera_src,
                                        usePiCamera=usePiCamera,
                                        resolution=resolution).start()
        time.sleep(2.0)

    def get_frame(self):
        return self.video_stream.read()

    def __del__(self):
        """

        Returns:

        """
        # show a message to the user
        print("[INFO] cleaning up...")
        self.video_stream.stop()
