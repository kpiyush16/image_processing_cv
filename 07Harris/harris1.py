from scipy import ndimage
import cv2
import numpy as np


def _compute_harris_response(image, eps=1e-6, gaussian_deviation=1):
    if len(image.shape) == 3:
        image = image.mean(axis=2)

    # derivatives
    image = ndimage.gaussian_filter(image, gaussian_deviation)
    imx = ndimage.sobel(image, axis=0, mode='constant')
    imy = ndimage.sobel(image, axis=1, mode='constant')

    Wxx = ndimage.gaussian_filter(imx * imx, 1.5, mode='constant')
    Wxy = ndimage.gaussian_filter(imx * imy, 1.5, mode='constant')
    Wyy = ndimage.gaussian_filter(imy * imy, 1.5, mode='constant')

    # determinant and trace
    Wdet = Wxx * Wyy - Wxy**2
    Wtr = Wxx + Wyy
    # Alternate formula for Harris response.
    # Alison Noble, "Descriptions of Image Surfaces", PhD thesis (1989)
    harris = Wdet / (Wtr + eps)

    return harris


def harris(image, min_distance=1, threshold=10, eps=1e-6,
           gaussian_deviation=1.5):

    harrisim = _compute_harris_response(image, eps=eps,
                    gaussian_deviation=gaussian_deviation)
    coordinates = ndimage.filters.maximum_filter(harrisim, min_distance)
    return coordinates

img = cv2.imread('Plaque.jpg', 1)
gray = cv2.imread("Plaque.jpg", 0)
gray = np.asarray(gray, dtype = 'float32')
dst = harris(gray)
#print (dst)
#dst = cv2.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,255]

cv2.imwrite('harris1.jpg',img)