import cv2
import numpy as np

# Load image
img = cv2.imread('HBD.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Compute Harris corner response
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Threshold the corner response
dst_thresh = dst > 0.01 * dst.max()

# Draw circles around the detected corners
img[dst_thresh] = [0, 0, 255]
img_with_corners = cv2.circle(img, (dst_thresh.shape[1]//2, dst_thresh.shape[0]//2), 10, (0, 255, 0), 2)

# Display image with detected corners
cv2.imshow('Image with Corners', img_with_corners)
cv2.waitKey(0)
cv2.destroyAllWindows()
