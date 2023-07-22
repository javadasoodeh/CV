import cv2
import numpy as np

# Load the two input images
foreground = cv2.imread('foreground.jpg')
background = cv2.imread('background.jpg')

# Resize the images to the same size
image1 = cv2.resize(foreground, (640, 480))
image2 = cv2.resize(background, (640, 480))

# Generate Gaussian pyramid for image1
G1 = image1.copy()
gp1 = [G1]
for i in range(3):
    G1 = cv2.pyrDown(G1)
    gp1.append(G1)

# Generate Gaussian pyramid for image2
G2 = image2.copy()
gp2 = [G2]
for i in range(3):
    G2 = cv2.pyrDown(G2)
    gp2.append(G2)

# Blend the images by combining pyramid levels
lp = []
for l1, l2 in zip(gp1, gp2):
    rows, cols, _ = l1.shape
    ls = np.hstack((l1[:, :cols//2], l2[:, cols//2:]))
    lp.append(ls)

# Reconstruct the blended image from the pyramid
blend = lp[0]
for i in range(1, 4):
    blend = cv2.pyrUp(blend)
    blend = cv2.add(blend, lp[i])

# Display the blended image
cv2.imshow('Blended Image', blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
