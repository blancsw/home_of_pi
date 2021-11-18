import cv2
from home_pi.motion_detection import MotionDetection

motion = MotionDetection("conf.json")

try:
    while True:
        motion_detect, obj = motion.get_frame()
        cv2.imshow("main", obj["frame"])
        cv2.waitKey(1)
except KeyboardInterrupt:
    print("Cleanup")
