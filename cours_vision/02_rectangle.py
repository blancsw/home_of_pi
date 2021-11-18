#!/usr/bin/env python
# -*- coding: utf-8 -*-

import imutils
from cv2 import cv2

IMG_PATH = "01.jpg"

img = cv2.imread(IMG_PATH)

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
