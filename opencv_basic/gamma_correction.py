import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('HBD.jpg')

# Define the gamma value
gamma = 2

# Apply gamma correction using the OpenCV LUT function
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
img_gamma_corrected = cv2.LUT(img, lookUpTable)

# Display the original and gamma-corrected images side by side
fig, ax = plt.subplots(1, 2)
ax[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
ax[0].set_title('Original Image')
ax[1].imshow(cv2.cvtColor(img_gamma_corrected, cv2.COLOR_BGR2RGB))
ax[1].set_title('Gamma-corrected Image (Gamma = {})'.format(gamma))
plt.show()