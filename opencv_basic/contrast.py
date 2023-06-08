import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image
img = cv2.imread('HBD.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Calculate the image mean and standard deviation
mean, std = cv2.meanStdDev(img)

# Calculate the contrast using the image mean and standard deviation
contrast = std / mean

# Check if the contrast is too low
if contrast < 0.5:
    print("Low contrast image detected")

# Display the image and histogram
plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Image')
plt.axis('off')
plt.subplot(122)
plt.plot(hist, color='black')
plt.title('Histogram')
plt.xlim([0, 256])
plt.xlabel('Pixel intensity')
plt.ylabel('Frequency')
plt.show()