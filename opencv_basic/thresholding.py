import cv2

# Read the input image
image = cv2.imread('HBD.jpg', 0)  # Load image in grayscale mode

# Apply different thresholding techniques
_, binary_threshold = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
_, binary_inverse_threshold = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
_, trunc_threshold = cv2.threshold(image, 128, 255, cv2.THRESH_TRUNC)
_, to_zero_threshold = cv2.threshold(image, 128, 255, cv2.THRESH_TOZERO)
_, to_zero_inverse_threshold = cv2.threshold(image, 128, 255, cv2.THRESH_TOZERO_INV)

# Otsu's thresholding
_, otsu_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the input and thresholded images
cv2.imshow('Input Image', image)
cv2.imshow('Binary Threshold', binary_threshold)
cv2.imshow('Binary Inverse Threshold', binary_inverse_threshold)
cv2.imshow('Trunc Threshold', trunc_threshold)
cv2.imshow('To Zero Threshold', to_zero_threshold)
cv2.imshow('To Zero Inverse Threshold', to_zero_inverse_threshold)
cv2.imshow("Otsu's Threshold", otsu_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
