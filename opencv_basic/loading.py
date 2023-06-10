import cv2

# Load the image using OpenCV
img = cv2.imread("HBD.jpg")

# Get the image dimensions
height, width, channels = img.shape

# Display the image dimensions
print(f"Input image dimensions: {width} x {height} x {channels}")

# Save the image to a new file
cv2.imwrite("output.jpg", img)
print("Image saved as output.jpg")
