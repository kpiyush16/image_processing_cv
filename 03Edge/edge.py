import cv2
import numpy as np

gray = cv2.imread('gray_image.jpg', 0)

def conv_transform(image):
	image_c = image.copy()
	for i in range(image.shape[0]):
		for j in range(image.shape[1]):
			image_c[i][j] = image[image.shape[0]-i-1][image.shape[1]-j-1]
	return image_c

def conv(image, kernel):
	kernel = conv_transform(kernel)
	image_h = image.shape[0]
	image_w = image.shape[1]

	kernel_h = kernel.shape[0]
	kernel_w = kernel.shape[1]

	h = kernel_h//2
	w = kernel_w//2

	image_conv = np.zeros(image.shape)
	for i in range(h, image_h-h):
		for j in range(w, image_w-w):
			sum = 0

			for m in range(kernel_h):
				for n in range(kernel_w):
					sum += kernel[m][n]*image[i-h+m][j-w+n]


			image_conv[i][j] = sum

	return image_conv

def norm(img1, img2):
	img_c = np.zeros(img1.shape)
	for i in range(img1.shape[0]):
		for j in range(img1.shape[1]):
			q = (img1[i][j]**2 + img2[i][j]**2)**0.5
			if q > 150:
				img_c[i][j] = 255
			else:
				img_c[i][j] = 0


	return img_c

kh = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype = np.float)
#kh = kh.T
kv = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype = np.float)
#kv = kv.T
gx = conv(gray, kh)
gy = conv(gray, kv)
norm = norm(gx, gy)


cv2.imwrite("sobelx.jpg", gx)
cv2.imwrite("sobely.jpg", gy)
cv2.imwrite("grad_magnitude.jpg", norm)