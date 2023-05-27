import cv2
import numpy as np

# Load the image
image = cv2.imread('HBD.jpg')

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Apply various blurring techniques

# 1. Averaging
kernel_size = (5, 5)
blurred_avg = cv2.blur(image, kernel_size)

# 2. Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, kernel_size, 0)

# 3. Median Blur
median_blur = cv2.medianBlur(image, 5)

# 4. Bilateral Filter
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)

# Display the blurred images
cv2.imshow('Averaging', blurred_avg)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Filter', bilateral_filter)
cv2.waitKey(0)

cv2.destroyAllWindows()
