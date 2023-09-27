import cv2

# Load the image using OpenCV
image = cv2.imread("../img/HBD.jpg")

# Get the value of a specific pixel
pixel_value = image[100, 100]
blue_value, green_value, red_value = pixel_value
print("Pixel value at (100, 100): Blue = {}, Green = {}, Red = {}".format(blue_value, green_value, red_value))

# Set the value of a specific pixel
image[100, 100] = [255, 0, 0]  # set the pixel to blue

# Get the values of a range of pixels
pixel_values = image[50:100, 50:100]
print("Pixel values in range (50-100, 50-100):")
for row in pixel_values:
    for pixel in row:
        blue_value, green_value, red_value = pixel
        print("Blue = {}, Green = {}, Red = {}".format(blue_value, green_value, red_value))

# Set the values of a range of pixels
image[50:100, 50:100] = [0, 255, 0]  # set the pixels to green

# Get the shape of the image
height, width, channels = image.shape
print("Image shape: Height = {}, Width = {}, Channels = {}".format(height, width, channels))

# Show the modified image
cv2.imshow("Modified Image", image)
cv2.waitKey(0)
