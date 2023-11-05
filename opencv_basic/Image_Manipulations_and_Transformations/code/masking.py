import cv2
import numpy as np

# Load the image
image = cv2.imread('../img/HBD.jpg')

# Create a mask (binary image) with a rectangular region of interest (ROI)
mask = np.zeros(image.shape[:2], dtype=np.uint8)
roi = (80, 100, 360, 300)  # (x, y, width, height)
cv2.rectangle(mask, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), 255, -1)

# Apply the mask to the image
masked_image = cv2.bitwise_and(image, image, mask=mask)

# Display the original image and the masked image
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
