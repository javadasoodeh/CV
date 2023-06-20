import cv2

# Load the input image
img = cv2.imread('HBD.jpg')

# Initialize the SIFT detector
sift = cv2.SIFT_create(nfeatures=0, nOctaveLayers=3, contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(img, None)

# Draw keypoints on the input image
img_with_keypoints = cv2.drawKeypoints(img, keypoints, None)

# Display the input image with keypoints
cv2.imshow('Input image with keypoints', img_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()