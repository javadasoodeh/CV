import cv2
import numpy as np

# Load the image
image = cv2.imread('HBD.jpg')

# Split the image into channels
b, g, r = cv2.split(image)

# Create an empty image with only the blue channel
blue_channel = np.zeros_like(image)
blue_channel[:, :, 0] = b

# Create an empty image with only the green channel
green_channel = np.zeros_like(image)
green_channel[:, :, 1] = g

# Create an empty image with only the red channel
red_channel = np.zeros_like(image)
red_channel[:, :, 2] = r

# Merge the channels back into an image
merged_image = cv2.merge([b, g, r])

# Display the original image and the split/merged images
cv2.imshow('Original Image', image)
cv2.imshow('Blue Channel', blue_channel)
cv2.imshow('Green Channel', green_channel)
cv2.imshow('Red Channel', red_channel)
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
