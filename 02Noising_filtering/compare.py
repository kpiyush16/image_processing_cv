import cv2
import math as ma
import numpy as np

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err


img1 = cv2.imread('gray_image.jpg', 0)
img2 = cv2.imread('g_filter.jpg', 0)
img3 = cv2.imread('m_filter.jpg', 0)
img4 = cv2.imread('noisy_image.jpg', 0)
psnr_g = (10 * ma.log10((255**2)/mse(img1, img2)))

psnr_m = (10 * ma.log10((255**2)/mse(img1, img3)))
psnr_n = (10 * ma.log10((255**2)/mse(img1, img4)))
print("psnr with noise = " + str(psnr_n)[:6], "\npsnr with median = " + str(psnr_m)[:6], "\npsnr with gauss = " + str(psnr_g)[:6])
