import cv2
import numpy as np

# Load two images
img1 = cv2.imread('HBD.jpg')
img2 = cv2.imread('HBD.jpg')

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Initialize the ORB feature detector and descriptor
orb = cv2.ORB_create()

# Detect keypoints and compute descriptors for both images
kp1, des1 = orb.detectAndCompute(gray1, None)
kp2, des2 = orb.detectAndCompute(gray2, None)

# Initialize the brute-force matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Select top matches
good_matches = matches[:50]

# Extract keypoints from good matches
src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# Compute homography matrix using RANSAC algorithm
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Apply homography to img1 to align it with img2
aligned_img1 = cv2.warpPerspective(img1, M, (img2.shape[1], img2.shape[0]))

# Display the aligned images side by side
aligned_images = np.hstack((aligned_img1, img2))
cv2.imshow('Aligned Images', aligned_images)
cv2.waitKey(0)
cv2.destroyAllWindows()