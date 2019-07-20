import cv2
import numpy as np

img1 = cv2.imread("1.jpg")
img2 = cv2.imread("2.jpg")

img1b = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2b = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

img3 =img1b-img2b
cv2.imshow("match",img3)
