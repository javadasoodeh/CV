import cv2
import numpy as np

# Load the two images to be blended
foreground = cv2.imread('foreground.jpg')
background = cv2.imread('background.jpg')

# Resize the images to the same size
foreground = cv2.resize(foreground, (640, 480))
background = cv2.resize(background, (640, 480))

# Set the weights for each image (alpha and beta)
alpha = 0.5
beta = 0.5

# Set the scalar value added to each pixel after blending (gamma)
gamma = 0


# if alpha and beta are going to be an numpy array
# def customAddWeighted(src1:np.ndarray, alpha: np.ndarray, src2:np.ndarray, beta: np.ndarray, gamma=0):
#     # Check if the images have the same size
#     if src1.shape != src2.shape:
#         raise ValueError("Input images must have the same size.")
#
#     # Perform alpha blending
#     blended_image = np.clip(src1 * alpha[:, :, np.newaxis] + src2 * beta[:, :, np.newaxis] + gamma, 0, 255).astype(
#         np.uint8)
#
#     return blended_image

def add_weighted(src1, alpha, src2, beta, gamma):
    # Check if the input images have the same size and type
    if src1.shape != src2.shape or src1.dtype != src2.dtype:
        raise ValueError("Input images must have the same size and type")

    # # Slow
    # # Compute the blended output image using loops
    # # Create an output image with the same size and type as the input images
    # dst = np.zeros(src1.shape, dtype=src1.dtype)
    #
    # # Loop through each pixel and blend the images using the formula
    # for i in range(src1.shape[0]):
    #     for j in range(src1.shape[1]):
    #         dst[i, j] = alpha * src1[i, j] + beta * src2[i, j] + gamma

    # Fast
    # Compute the blended output image using NumPy vectorization
    dst = alpha * src1.astype(np.float32) + beta * src2.astype(np.float32) + gamma
    dst = np.clip(dst, 0, 255).astype(src1.dtype)

    return dst


# Blend the two images using the addWeighted function
blended_img = add_weighted(foreground, alpha, background, beta, gamma)
# blended_img = cv2.addWeighted(foreground, alpha, background, beta, gamma)

# Display the blended image
cv2.imshow('Blended Image', blended_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
