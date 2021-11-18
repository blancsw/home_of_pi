#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imutils
from cv2 import cv2

IMG_PATH = "01.jpg"

img = imutils.resize(cv2.imread(IMG_PATH), 600)
cv2.imshow("main", img)
cv2.waitKey(0)

# -------------------------------------------------------------

# Blue: 0
# Green: 1
# Red: 2


bleu_img = imutils.resize(img, 600)
# Green
bleu_img[:, :, 1] = 0
# Red
bleu_img[:, :, 2] = 0

cv2.imshow("main", bleu_img)
cv2.waitKey(0)


# -------------------------------------------------------------

img = cv2.imread("bg.png")
img2 = imutils.resize(cv2.imread("cat.png"), 200)
(h, w) = img2.shape[:2]

img[100:100 + h, 100:100 + w] = img2
cv2.imshow("main", img)
cv2.waitKey(0)