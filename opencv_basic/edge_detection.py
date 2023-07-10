import cv2

# Specify the path to your image
image_path = 'HBD.jpg'

# Load the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display the original image and the edge-detected image
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)

# Wait for key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()


