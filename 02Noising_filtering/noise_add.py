import numpy as np
import os
import cv2


def noise(image, sigma):
	row,col,ch= image.shape
	mean = 0
	gauss = np.random.normal(mean,sigma,(row,col,ch))
	gauss = gauss.reshape(row,col,ch)
	noisy = image + gauss
	return noisy


gray = cv2.imread("gray_image.jpg")
noised = noise(gray, 5)

cv2.imwrite("noisy_image.jpg", noised)