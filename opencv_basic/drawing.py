import cv2
import numpy as np

# Create a black image with dimensions 300x400 and 3 channels
height, width = 300, 400
channels = 3
image = np.zeros((height, width, channels), dtype=np.uint8)

height, width, channels = image.shape

# Draw a line
start_point = (0, 0)
end_point = (width, height)
color = (0, 0, 255)
thickness = 2
cv2.line(image, start_point, end_point, color, thickness)
# Parameters: image, start_point, end_point, color, thickness

# Draw a rectangle
top_left = (50, 50)
bottom_right = (150, 150)
color = (0, 255, 0)
thickness = 3
cv2.rectangle(image, top_left, bottom_right, color, thickness)
# Parameters: image, top_left, bottom_right, color, thickness

# Draw a square
top_left = (200, 50)
side_length = 50
color = (255, 0, 0)
thickness = -1
bottom_right = (top_left[0] + side_length, top_left[1] + side_length)
cv2.rectangle(image, top_left, bottom_right, color, thickness)
# Parameters: image, top_left, bottom_right, color, thickness

# Create 10 random circles
for i in range(10):
    center = (np.random.randint(0, width), np.random.randint(0, height))
    radius = np.random.randint(10, 50)
    color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
    thickness = -1

    cv2.circle(image, center, radius, color, thickness)
    # Parameters: image, center, radius, color, thickness

# Show the image
cv2.imshow("Shapes", image)
cv2.waitKey(0)