import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the input image
img = cv2.imread('HBD.jpg')

# Convert the image to LAB color space
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Split the LAB image into its three channels
l_channel, a_channel, b_channel = cv2.split(lab_img)

# Histogram equalize the L channel
l_channel_eq = cv2.equalizeHist(l_channel)

# Merge the histogram-equalized L channel with the original A and B channels
lab_img_eq = cv2.merge((l_channel_eq, a_channel, b_channel))

# Convert the LAB image back to RGB
output_img = cv2.cvtColor(lab_img_eq, cv2.COLOR_LAB2BGR)

# Display the original and output images using Matplotlib
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Automatic Color Correction')

ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax1.set_title('Input Image')

ax2.imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
ax2.set_title('Output Image')

plt.show()