import cv2
import numpy as np

img = cv2.imread('gray_image.jpg',0)
histogram = cv2.equalizeHist(img)

cv2.imwrite('histogram.jpg',histogram)