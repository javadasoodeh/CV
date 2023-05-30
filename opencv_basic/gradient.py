import cv2
import numpy as np

# Load the image
image = cv2.imread('HBD.jpg', cv2.IMREAD_GRAYSCALE)

# Convert the image to float32
image = np.float32(image)

# Calculate the gradient in x and y directions
gradient_x = cv2.Sobel(image, cv2.CV_32F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(image, cv2.CV_32F, 0, 1, ksize=3)

# Calculate the magnitude of the gradient
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)

# Normalize the gradient magnitude for display
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Display the original image and the gradient magnitude
cv2.imshow('Original Image', image.astype(np.uint8))
cv2.imshow('Gradient Magnitude', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()
