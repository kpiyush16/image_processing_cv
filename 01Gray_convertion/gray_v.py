
import cv2

gray = cv2.imread('Plaque.jpg', 0)
cv2.imwrite("gray_image_v.jpg", gray)