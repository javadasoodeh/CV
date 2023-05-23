import cv2
import numpy as np

# Load two grayscale images
image1 = cv2.imread('HBD.jpg', cv2.IMREAD_GRAYSCALE)
# Create a second image with all values set to 20
image2 = np.full_like(image1, 20)

# Perform arithmetic operations using NumPy
addition_numpy = np.add(image1, image2)
subtraction_numpy = np.subtract(image1, image2)
multiplication_numpy = np.multiply(image1, image2)
division_numpy = np.divide(image1, image2)

# Perform arithmetic operations using OpenCV
addition_opencv = cv2.add(image1, image2)
subtraction_opencv = cv2.subtract(image1, image2)
multiplication_opencv = cv2.multiply(image1, image2)
division_opencv = cv2.divide(image1, image2)

# Display the images and arithmetic results
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Addition (NumPy)', addition_numpy)
cv2.imshow('Subtraction (NumPy)', subtraction_numpy)
cv2.imshow('Multiplication (NumPy)', multiplication_numpy)
cv2.imshow('Division (NumPy)', division_numpy)
cv2.imshow('Addition (OpenCV)', addition_opencv)
cv2.imshow('Subtraction (OpenCV)', subtraction_opencv)
cv2.imshow('Multiplication (OpenCV)', multiplication_opencv)
cv2.imshow('Division (OpenCV)', division_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()
