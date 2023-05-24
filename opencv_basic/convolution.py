import cv2
import numpy as np


def convolution(image, kernel):
    image_height, image_width = image.shape[:2]
    kernel_height, kernel_width = kernel.shape[:2]

    # Pad the image to handle border effects
    padding_height = kernel_height // 2
    padding_width = kernel_width // 2
    padded_image = cv2.copyMakeBorder(image, padding_height, padding_height, padding_width, padding_width,
                                      cv2.BORDER_CONSTANT)

    # Create an output image with the same shape as the input image
    output = np.zeros_like(image, dtype=np.float32)

    # Perform convolution
    for y in range(image_height):
        for x in range(image_width):
            # Extract the region of interest from the padded image
            roi = padded_image[y:y + kernel_height, x:x + kernel_width]

            # Perform element-wise multiplication between the kernel and the ROI
            result = np.sum(np.multiply(roi, kernel))

            # Store the result in the output image
            output[y, x] = result

    return output

# Load an image
image = cv2.imread('HBD.jpg', cv2.IMREAD_GRAYSCALE)


# Define a kernel (3x3 Gaussian blur filter)
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]) / 16.0

# Apply the convolution operation
output = convolution(image, kernel)

# Convert the output image to 8-bit unsigned integer (grayscale)
output = np.uint8(output)

# Display the original image and the convolved image
cv2.imshow('Original Image', image)
cv2.imshow('Convolved Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
