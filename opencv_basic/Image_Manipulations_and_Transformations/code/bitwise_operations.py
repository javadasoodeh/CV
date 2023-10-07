import cv2
import numpy as np

# Create two binary images
image1 = np.zeros((300, 300), dtype=np.uint8)
image1[50:150, 100:200] = 255

image2 = np.zeros((300, 300), dtype=np.uint8)
image2[100:200, 150:250] = 255

# Perform bitwise AND
bitwise_and = cv2.bitwise_and(image1, image2)

# Perform bitwise OR
bitwise_or = cv2.bitwise_or(image1, image2)

# Perform bitwise XOR
bitwise_xor = cv2.bitwise_xor(image1, image2)

# Perform bitwise NOT
bitwise_not = cv2.bitwise_not(image1)

# Display the original images and bitwise operations
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise XOR', bitwise_xor)
cv2.imshow('Bitwise NOT', bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
