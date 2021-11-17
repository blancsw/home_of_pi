import os

from gpiozero import PWMLED

from home_pi.motion_detection import MotionDetection

FOLDER_ABSOLUTE_PATH = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

CONF_PATH = os.path.join(FOLDER_ABSOLUTE_PATH, "conf.json")
SAVE_PATH = FOLDER_ABSOLUTE_PATH

led_move = PWMLED(17)
led_not_move = PWMLED(4)

motion = MotionDetection(CONF_PATH)
print("start loop")
try:
    while True:
        motion_detect, obj = motion.get_frame()
        """
        Example d'utilisation
        x = obj["x"]
        y = obj["y"]
        width = obj["width"]
        height = obj["height"]
        frame = obj["frame"]
        cv2.rectangle(img=,
                pt1=,
                pt2=,
                color=motion.GREEN_COLOR,
                thickness=2)
        cv2.imwrite("toto.jpg", frame)
        """
except KeyboardInterrupt:
    print("Cleanup")
    motion.stop()
