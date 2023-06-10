import cv2
import numpy as np

# Load the two images to be blended
img1 = cv2.imread('HBD.jpg')
img2 = cv2.imread('HBD.jpg')

# Resize the images to the same size
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

# Create a mask image of the same size as the images
mask = np.zeros((480, 640), dtype=np.uint8)

# Draw a rectangle on the mask
cv2.rectangle(mask, (100, 100), (540, 380), (255, 255, 255), -1)

# Convert the mask to a float image
mask = mask.astype(float) / 255.0

# Perform alpha blending with the two images using the mask
blended = cv2.addWeighted(img1, 1.0 - mask, img2, mask, 0.0)

# Display the blended image
cv2.imshow('Blended Image', blended)

cv2.waitKey(0)

cv2.destroyAllWindows()