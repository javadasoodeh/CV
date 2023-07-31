import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the image
image_path = 'HBD.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the histogram for grayscale image
hist_gray, bins_gray = np.histogram(gray_image.flatten(), 256, [0, 256])

# Create a plot
plt.figure(figsize=(8, 6))

# Show the grayscale image
plt.subplot(2, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

# Plot the histogram for grayscale image
plt.subplot(2, 2, 2)
plt.plot(hist_gray, color='gray')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Grayscale Image Histogram')

# Calculate the 2D histogram for color image
chans = cv2.split(image)
hist_2d = cv2.calcHist([chans[0], chans[1]], [0, 1], None, [32, 32], [0, 256, 0, 256])

# Show the selected color channels (blue and green)
plt.subplot(2, 2, 3)
plt.imshow(cv2.merge([chans[0], chans[1], np.zeros_like(chans[0])]))  # Show only the first two color channels
plt.title('Color Channels (Ch1/Blue, Ch2/Green)')

# Plot the 2D histogram for color image
plt.subplot(2, 2, 4)
plt.imshow(hist_2d, interpolation='nearest', cmap='jet')
plt.colorbar()
plt.xlabel('Channel 1')
plt.ylabel('Channel 2')
plt.title('2D Color Histogram')

plt.tight_layout()
plt.show()


fig = plt.figure()
hist_3d = cv2.calcHist(chans, [0, 1, 2], None, [32, 32, 32], [0, 256, 0, 256, 0, 256])
ax = fig.add_subplot(1, 2, 1, projection='3d')
hist_3d = hist_3d.flatten()
colors = np.array([[(i, j, k) for i in range(32)] for j in range(32) for k in range(32)]).reshape(-1, 3)
positions = np.array([[(i, j, k) for i in range(32)] for j in range(32) for k in range(32)]).reshape(-1, 3)
ax.bar3d(positions[:, 0], positions[:, 1], positions[:, 2], 1, 1, hist_3d, color=colors / 32)

fig.add_subplot(1, 2, 2)
plt.imshow(image)
plt.title('3 Channels Image')
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
