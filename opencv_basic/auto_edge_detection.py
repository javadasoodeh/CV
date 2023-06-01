import cv2
import numpy as np

# Load image
img = cv2.imread("HBD.jpg")

# Auto Canny edge detection with wide threshold
edges_wide = cv2.Canny(img, 10, 200)

# Auto Canny edge detection with tight threshold
edges_tight = cv2.Canny(img, 50, 150)

# Compute median of image pixel intensities
median = np.median(img)

# Set lower and upper thresholds using median intensity
lower_threshold = int(max(0, (1.0 - 0.33) * median))
upper_threshold = int(min(255, (1.0 + 0.33) * median))

# Auto Canny edge detection with automatic thresholding
edges_auto = cv2.Canny(img, lower_threshold, upper_threshold)

# Display images
cv2.imshow('Original', img)
cv2.imshow('Wide Threshold', edges_wide)
cv2.imshow('Tight Threshold', edges_tight)
cv2.imshow('Auto Threshold', edges_auto)
cv2.waitKey(0)
cv2.destroyAllWindows()