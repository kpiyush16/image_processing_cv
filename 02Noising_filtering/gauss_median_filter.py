from skimage import filters, io
import cv2


img_array = io.imread('noise_add.py.jpg')
g_blur = filters.gaussian(img_array, sigma=4, output=None, mode='nearest', cval=0, multichannel=None, preserve_range=False, truncate=4.0)
io.imsave('g_filter.jpg', g_blur)


image = cv2.imread('noise_add.py.jpg')
median = cv2.medianBlur(image,5)
cv2.imwrite('m_filter.jpg', median)
