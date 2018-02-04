# image_processing_cv
Advanced Digital Image Processing and Computer Vision

#####Image Processing Fundamentals#####

Requirements: OpenCV, Python standard libraries and LINUX based Kernel 
FileName: MyProject.tar.gz

#01Gray_conversion:
-> The "gray.py" converts RGB image to Gray Image.

#02Noising_filtering:
-> "noise_add.py" will add random gaussian noise of STD 5 on the gray image.
-> "gauss_median_filter.py" will filter out the noisy image with STD 5 and 4 respectively.
-> "compare.py" will compare the PSNR values of Gaussian filtered, Median filtered and Noisy image w.r.t. the original gray image.

#03Edge:
-> "edge.py" will apply sobel and prewitt operators to obtain x_gradient, y_gradient and gradient_magitude as well as will obtain thesholded image with certain optimum threshold.

#04LoG_ZC:
-> "LoG.py" will obtain Laplace of Gaussian as well as Zero Crossing applied images.

#05Text_Extract:
-> "water.py" will firstly invert the gray_image to obtain its compliment and obtain the background as well as foreground images and will mark out the segmented portion with Blue Marker buy using watershed Algorithm.
-> "text_extract.py" will accept the 'image' argument and will crop the text region of the image to obtain the cropped image respectively.

#06Enhancing:
-> "alpha_rooting.py" will use the background and foreground images from gray_image generated and thereby generating enhanced alpha rooted image "alpha_rooted.jpg".
-> "histogram.py" will apply histogram broadening of gray_image and will enhance the image "histogram.jpg".

#07Harris:
-> "harris1.py" and "harris2.py" will point out the corner points in 2 ways on the figure with kernel size '3' and will save it to "harris1.jpg" and "harris2.jpg".
