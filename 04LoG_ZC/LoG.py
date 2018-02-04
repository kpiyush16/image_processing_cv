from scipy import signal
import scipy.ndimage as nd
import numpy as np
import matplotlib.pyplot as plt
import cv2
from cv2 import getGaussianKernel, CV_64F
import scipy




def crossings(image, kernel, threshold):
    result = np.empty(image.shape, dtype=np.float32)
    def convolution(i, j, res, kern):
        c = np.sum(np.multiply(np.asfarray(res), kern))
        result[i,j] = c

    frame(image, kernel, convolution)

    output = np.empty(result.shape, dtype=np.uint8)
    def thresholding(i, j, res, kern):
        center = result[i,j]
        output[i,j] = 255
        if center > threshold:
            if np.count_nonzero(res < -threshold) > 0:
                output[i,j] = 0
        elif center < -threshold:
            if np.count_nonzero(res > threshold) > 0:
                output[i,j] = 0

    frame(result, np.ones((3,3),dtype=np.uint8), thresholding)
    return output


def laplacian_of_gaussian(image):
    kernel = np.array([[ 0,0,1,0,0],
                       [ 0,1,2,1,0],
                       [ 1,2,-16,2,1],
                       [0,1,2,1,0],
                       [0,0,1,0,0]],
                       dtype=np.float32)
    return crossings(image, kernel, 127)
    

def difference_of_gaussian(image):
    def gkernel(size = 11, sigma = 0.95):
        mat = getGaussianKernel(size, sigma, CV_64F)
        return np.dot(mat, np.transpose(mat))
    dog = gkernel(sigma=0.95) - gkernel(sigma=2.75)
    return crossings(image, dog, 2.75)


def frame(image, kernel, function):
    offset = np.divide(np.subtract(kernel.shape, 1), 2)
    for i, j in np.ndindex(image.shape):
        i1, j1 = np.fmax(np.subtract((i,j), offset), (0,0))
        i2, j2 = np.fmin(np.add((i+1,j+1), offset), image.shape)
        res = image[int(i1):int(i2), int(j1):int(j2)]
        k1 = np.add(np.subtract((i1,j1), (i,j)), offset)
        k2 = np.add(res.shape, k1)
        kernel2 = kernel[int(k1[0]):int(k2[0]), int(k1[1]):int(k2[1])]
        function(i, j, res, kernel2)


image = cv2.imread('gray_image.jpg', 0)

l = laplacian_of_gaussian(image)
cv2.imwrite('laplacian-of-gaussian.jpg', l)
    
d = difference_of_gaussian(image)
cv2.imwrite('zero_crossings.jpg', d)