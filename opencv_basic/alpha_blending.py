import cv2
import numpy as np

# Load the two images to be blended
foreground = cv2.imread('foreground.jpg')
background = cv2.imread('background.jpg')

# Resize the images to the same size
foreground = cv2.resize(foreground, (640, 480))
background = cv2.resize(background, (640, 480))

# Create a mask image of the same size as the images
mask = np.zeros((480, 640), dtype=np.uint8)

# Draw a rectangle on the mask
cv2.rectangle(mask, (100, 100), (600, 400), (255, 255, 255), -1)

# Convert the mask to a float image
alpha_mask = mask.astype(float) / 255.0

# alpha_array = np.ones(foreground.shape[:2]) * 0.5  # Array of same size as foreground, filled with 0.5
# beta_array = np.ones(background.shape[:2]) * 0.5

# Resize the foreground and background images to match the alpha mask size
foreground = cv2.resize(foreground, (alpha_mask.shape[1], alpha_mask.shape[0]))
background = cv2.resize(background, (alpha_mask.shape[1], alpha_mask.shape[0]))


def customAddWeighted(src1, alpha, src2, beta, gamma=0):
    # Check if the images have the same size
    if src1.shape != src2.shape:
        raise ValueError("Input images must have the same size.")

    # Perform alpha blending
    blended_image = np.clip(src1 * alpha[:, :, np.newaxis] + src2 * beta[:, :, np.newaxis] + gamma, 0, 255).astype(
        np.uint8)

    return blended_image


# Perform alpha blending using the mask
blended_image = customAddWeighted(foreground, alpha_mask, background, 1 - alpha_mask)

# Display the blended image
cv2.imshow('Blended Image', blended_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
