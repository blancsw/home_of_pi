
import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    # # Largeur
    # start_x = 100
    # # hauteur
    # start_y = 300
    #
    # # Largeur
    # end_x = start_x + 100
    # # Heuteur
    # end_y = start_y + 50
    #
    # cv2.rectangle(img=frame,
    #               pt1=(start_x, start_y),
    #               pt2=(end_x, end_y),
    #               color=(255, 0, 144),
    #               thickness=2)

    cv2.imshow("main", frame)
    cv2.waitKey(1)
