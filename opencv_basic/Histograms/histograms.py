import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'colorful.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate the histogram for grayscale image
hist_gray = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Create a plot
plt.figure(figsize=(10, 4))

# Show the grayscale image
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

# Plot the histogram for grayscale image
plt.subplot(1, 2, 2)
plt.plot(hist_gray, color='gray')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Grayscale Image Histogram')
plt.show()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Create a plot
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.imshow(image, aspect='auto')
plt.title('RGB Image')
plt.axis('off')

plt.subplot(1, 2, 2)
# Calculate and plot the histogram for each channel
colors = ('r', 'g', 'b')
for i, color in enumerate(colors):
    histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)

plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Color Histogram (R, G, B)')
plt.show()


# Create a plot
plt.figure(figsize=(12, 4))

hist_size = 32
# Calculate the 2D histogram for color image
channels = cv2.split(image)
colors = ['R', 'G', 'B']
for i, mixed_channels in enumerate([(0, 1), (1, 2), (0, 2)]):
    plt.subplot(1, 3, i + 1)
    hist_2d = cv2.calcHist([channels[mixed_channels[0]], channels[mixed_channels[1]]], [0, 1], None, [hist_size, hist_size], [0, 256, 0, 256])
    # Plot the 2D histogram for color image
    plt.imshow(hist_2d, interpolation='nearest', cmap='jet')
    plt.colorbar()
    plt.xlabel('Channel {}'.format(mixed_channels[0]))
    plt.ylabel('Channel {}'.format(mixed_channels[1]))
    plt.title('2D Color Histogram {} & {}'.format(colors[mixed_channels[0]], colors[mixed_channels[1]]))

# Automatically adjust the layout
plt.tight_layout()

plt.show()

# Create a plot
plt.figure()

# Create a 3D histogram with 32 bins in each dimension (change as needed)
hist_size = 8
hist = cv2.calcHist([channels[0], channels[1], channels[2]], [0, 1, 2], None, [hist_size, hist_size, hist_size], [0, 256, 0, 256, 0, 256])

# Find the nonzero elements
non_zero = np.where(hist > 0)

# Get the frequency values for the nonzero elements
frequencies = hist[non_zero]

# Create a 3D scatter plot
ax = plt.subplot(1, 1, 1, projection='3d')

# Scatter plot, using the non-zero values and frequencies
ax.scatter(non_zero[0], non_zero[1], non_zero[2], c=frequencies.flatten(), cmap='viridis', marker='o')

# Set labels
ax.set_xlabel('Red Channel')
ax.set_ylabel('Green Channel')
ax.set_zlabel('Blue Channel')

# Add colorbar to represent frequency
plt.colorbar(ax.scatter(non_zero[0], non_zero[1], non_zero[2], c=frequencies.flatten(), cmap='viridis'), ax=ax)

plt.show()
