import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the reference and input images
ref_image = cv2.imread('Koala.jpg', cv2.IMREAD_GRAYSCALE)
input_image = cv2.imread('HBD.jpg', cv2.IMREAD_GRAYSCALE)

# Perform histogram equalization on the reference image
ref_hist, _ = np.histogram(ref_image.flatten(), 256, [0, 256])
ref_cdf = np.cumsum(ref_hist)
ref_cdf_normalized = ref_cdf / ref_cdf.max()
ref_equalized = np.interp(ref_image.flatten(), range(256), ref_cdf_normalized).reshape(ref_image.shape)

# Perform histogram matching on the input image using the reference image
input_hist, _ = np.histogram(input_image.flatten(), 256, [0, 256])
input_cdf = np.cumsum(input_hist)
input_cdf_normalized = input_cdf / input_cdf.max()
matched = np.interp(input_cdf_normalized, ref_cdf_normalized, range(256)).astype('uint8')
matched_image = matched[input_image]

# Display the original and matched images side by side
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(input_image, cmap='gray')
axs[0].set_title('Input Image')
axs[1].imshow(matched_image, cmap='gray')
axs[1].set_title('Matched Image')
plt.show()