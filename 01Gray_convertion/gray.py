import numpy as np
import matplotlib.pyplot as plt
import cv2

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = cv2.imread('Plaque.jpg')     
gray = rgb2gray(img)
cv2.imwrite("gray_image.jpg", gray)

