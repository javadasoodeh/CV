import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('moon-orange.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate and display the histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.figure()
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(hist)

# Apply adaptive histogram equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
equalized_image = clahe.apply(image)

# Display the original and equalized images
plt.figure()
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(122)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')

# Calculate and display the equalized histogram
equalized_hist = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
plt.figure()
plt.title('Equalized Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.plot(equalized_hist)

# Show all plots
plt.show()
