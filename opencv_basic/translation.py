import argparse
import cv2
import numpy as np


# Load the input image using the file path argument
img = cv2.imread("HBD.JPG")

# Get the image dimensions
rows, cols = img.shape[:2]

# Define the translation matrix
# Move the image up and right by 100 pixels
M1 = np.float32([[1, 0, 100], [0, 1, -100]])

# Define the translation matrix
# Move the image down and left by 100 pixels
M2 = np.float32([[1, 0, -100], [0, 1, 100]])

# Apply the translation matrix to the image
# Move the image up and right
img_translated1 = cv2.warpAffine(img, M1, (cols, rows))

# Apply the translation matrix to the image
# Move the image down and left
img_translated2 = cv2.warpAffine(img, M2, (cols, rows))

# Display the original and translated images
cv2.imshow('Original Image', img)
cv2.imshow('Translated Image 1', img_translated1)
cv2.imshow('Translated Image 2', img_translated2)

# Wait for a key press and then exit
cv2.waitKey(0)
cv2.destroyAllWindows()