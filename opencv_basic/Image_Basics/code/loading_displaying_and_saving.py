import cv2

# Load the image using OpenCV
img = cv2.imread("../img/HBD.jpg")

# Get the image dimensions
height, width, channels = img.shape

# Display the image dimensions
print(f"Input image dimensions: {width} x {height} x {channels}")

# Displaying the image
cv2.imshow("Image", img)
cv2.waitKey(0)

# Save the image to a new file
cv2.imwrite("output.jpg", img)
print("Image saved as output.jpg")
