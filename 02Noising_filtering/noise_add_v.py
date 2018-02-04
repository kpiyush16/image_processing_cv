import cv2
import numpy as np
def noisy(image, std):
    row,col,ch= image.shape
    mean = 0

    gauss = np.random.normal(mean,std,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy

image = cv2.imread('gray_image.jpg')

noisy_img = noisy(image, 5)
cv2.imwrite('noisy_image_v.jpg',noisy_img)
