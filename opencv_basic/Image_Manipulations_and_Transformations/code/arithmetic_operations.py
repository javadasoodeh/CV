import cv2
import numpy as np

# Load a grayscale image
image1 = cv2.imread('../img/HBD.jpg', cv2.IMREAD_GRAYSCALE)
# Create a second image with all values set to 20
image2 = np.full_like(image1, 20)


def saturated_add(image1, image2):
    # Ensure the images have the same data type
    assert image1.dtype == image2.dtype, "Images must have the same data type"

    # Calculate the intermediate sum
    intermediate_sum = image1.astype(np.int16) + image2.astype(np.int16)

    # Clip the values to the range 0 to 255
    result = np.clip(intermediate_sum, 0, 255).astype(np.uint8)

    return result

# Perform arithmetic operations using NumPy
addition_numpy = saturated_add(image1, image2)
subtraction_numpy = np.subtract(image1, image2)
multiplication_numpy = np.multiply(image1, image2)
division_numpy = np.divide(image1, image2)

# Perform arithmetic operations using OpenCV
addition_opencv = cv2.add(image1, image2)
subtraction_opencv = cv2.subtract(image1, image2)
multiplication_opencv = cv2.multiply(image1, image2)
division_opencv = cv2.divide(image1, image2)

# Display the images and arithmetic results
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.waitKey(0)
cv2.imshow('Addition (NumPy)', addition_numpy)
cv2.imshow('Addition (OpenCV)', addition_opencv)
cv2.waitKey(0)
cv2.imshow('Subtraction (NumPy)', subtraction_numpy)
cv2.imshow('Subtraction (OpenCV)', subtraction_opencv)
cv2.waitKey(0)
cv2.imshow('Multiplication (NumPy)', multiplication_numpy)
cv2.imshow('Multiplication (OpenCV)', multiplication_opencv)
cv2.waitKey(0)
cv2.imshow('Division (NumPy)', division_numpy)
cv2.imshow('Division (OpenCV)', division_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()
