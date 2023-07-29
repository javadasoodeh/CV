import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'HBD.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_image)

# Calculate the histogram for grayscale image
hist_gray, bins_gray = np.histogram(gray_image.flatten(), 256, [0, 256])

# Plot the histogram for grayscale image
plt.figure(figsize=(8, 8))
plt.subplot(2, 2, 1)
plt.plot(hist_gray, color='gray')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Grayscale Image Histogram')

# Step 7: Calculate the 2D histogram for color image
chans = cv2.split(image)
hist_2d = cv2.calcHist([chans[0], chans[1]], [0, 1], None, [32, 32], [0, 256, 0, 256])

# Step 8: Plot the 2D histogram for color image
plt.subplot(2, 2, 2)
plt.imshow(hist_2d, interpolation='nearest', cmap='jet')
plt.colorbar()
plt.xlabel('Channel 1')
plt.ylabel('Channel 2')
plt.title('2D Color Histogram')

# Step 9: Show the grayscale image
plt.subplot(2, 2, 3)
plt.imshow(gray_image)
plt.title('Grayscale Image')

# Step 9: Show the selected color channels
plt.subplot(2, 2, 4)
plt.imshow(cv2.merge([chans[0], chans[1], np.zeros_like(chans[0])]))  # Show only the first two color channels
plt.title('Selected Color Channels (Ch1, Ch2)')

plt.tight_layout()
plt.show()

# Step 10: Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
