import cv2
# from gpiozero import PWMLED

from home_pi.motion_detection import MotionDetection

# led_move = PWMLED(17)
# led_not_move = PWMLED(4)

motion = MotionDetection("conf.json")

try:
    while True:
        motion_detect, obj = motion.get_frame()
        if motion_detect:
            # Draw rectangle
            cv2.rectangle(obj["frame"],
                          pt1=(obj["x"], obj["y"]),
                          pt2=(obj["x"] + obj["width"], obj["y"] + obj["height"]),
                          color=motion.GREEN_COLOR,
                          thickness=2)
            motion.save_frame(obj["frame"])
            # led_move.value = 1.0
            # led_not_move.value = 0.0
        else:
            pass
            # led_move.value = 0.0
            # led_not_move.value = 1.0
except KeyboardInterrupt:
    print("Cleanup")
