import cv2
import numpy as np

# Load an image
img = cv2.imread('HBD.jpg', cv2.IMREAD_GRAYSCALE)

# Define a kernel for erosion and dilation
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=1, borderType=cv2.BORDER_CONSTANT,
                    borderValue=0, anchor=(-1, -1))

# Apply dilation
dilation = cv2.dilate(img, kernel, iterations=1, borderType=cv2.BORDER_CONSTANT,
                      borderValue=0, anchor=(-1, -1))

# Apply opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1,
                           borderType=cv2.BORDER_CONSTANT, borderValue=0, anchor=(-1, -1),
                           )

# Apply closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=1,
                           borderType=cv2.BORDER_CONSTANT, borderValue=0, anchor=(-1, -1),
                           )

# Apply gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel, iterations=1,
                            borderType=cv2.BORDER_CONSTANT, borderValue=0, anchor=(-1, -1))

# Apply top hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel, iterations=1,
                          borderType=cv2.BORDER_CONSTANT, borderValue=0, anchor=(-1, -1),
                          )

# Apply black hat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel, iterations=1,
                            borderType=cv2.BORDER_CONSTANT, borderValue=0, anchor=(-1, -1),
                            )

# Display the original image and the results of the morphological operations
cv2.imshow('Original Image', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.imshow('Gradient', gradient)
cv2.imshow('Top Hat', tophat)
cv2.imshow('Black Hat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
