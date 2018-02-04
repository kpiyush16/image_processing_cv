import cv2
 
# Read the images
foreground = cv2.imread("foreground_image.jpg")
background = cv2.imread("background_image.jpg")

alpha = cv2.imread("gray_image.jpg", 0)
 
# Convert uint8 to float
foreground = foreground.astype(float)
background = background.astype(float)
 
# Normalize the alpha mask to keep intensity between 0 and 1
alpha = alpha.astype(float)/255
 
# Multiply the foreground with the alpha matte
foreground = cv2.multiply(alpha, foreground)
 
# Multiply the background with ( 1 - alpha )
background = cv2.multiply(1.0 - alpha, background)
 
# Add the masked foreground and background.
outImage = cv2.add(foreground, background)

cv2.imwrite("alpha_rooted.jpg", outImage)
