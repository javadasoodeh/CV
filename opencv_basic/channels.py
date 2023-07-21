import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('HBD.jpg')

# Split the image into channels
b, g, r = cv2.split(image)

# Create an empty image with only the blue channel
blue_channel = np.zeros_like(image)
blue_channel[:, :, 0] = b

# Create an empty image with only the green channel
green_channel = np.zeros_like(image)
green_channel[:, :, 1] = g

# Create an empty image with only the red channel
red_channel = np.zeros_like(image)
red_channel[:, :, 2] = r

# Merge the channels back into an image
merged_image = cv2.merge([b, g, r])

# Display the images using matplotlib
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Blue Channel
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(blue_channel, cv2.COLOR_BGR2RGB))
plt.title('Blue Channel')
plt.axis('off')

# Green Channel
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(green_channel, cv2.COLOR_BGR2RGB))
plt.title('Green Channel')
plt.axis('off')

# Red Channel
plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(red_channel, cv2.COLOR_BGR2RGB))
plt.title('Red Channel')
plt.axis('off')

# Merged Image
plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(merged_image, cv2.COLOR_BGR2RGB))
plt.title('Merged Image')
plt.axis('off')

plt.tight_layout()
plt.show()
