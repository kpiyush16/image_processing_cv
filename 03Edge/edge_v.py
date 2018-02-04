import cv2
import numpy as np

scale = 1
delta = 0
ddepth = cv2.CV_64F

gray = cv2.imread('gray_image.jpg', 0)

# Gradient-X
grad_x = cv2.Sobel(gray,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)


# Gradient-Y
grad_y = cv2.Sobel(gray,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)


abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
abs_grad_y = cv2.convertScaleAbs(grad_y)

dst = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)

cv2.imwrite("sobelx_v.jpg", grad_y)
cv2.imwrite("sobely_v.jpg", grad_x)
cv2.imwrite("grad_magnitude_v.jpg", dst)
