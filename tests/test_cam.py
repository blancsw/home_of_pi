# import the necessary packages
"""
Test pi cam

Usage:
  test_cam.py <out_name>

Options:
  -h --help     Show this screen.
  <out_name>    Output file name
"""

import time

import cv2
from docopt import docopt
from imutils.video import VideoStream

args = docopt(__doc__)

print("Starting video stream...")
vs = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)
frame = vs.read()
cv2.imwrite(args.get("<out_name>"), frame)
