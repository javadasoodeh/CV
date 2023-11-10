import cv2
import math
import numpy as np


# Optional(Just to know what is happening behind getRotationMatrix2D function)
def get_rotation_matrix(center, angle, scale):
    # Convert the angle to radians
    theta = math.radians(angle)

    # Extract the center coordinates
    center_x, center_y = center

    # Calculate sine and cosine of the angle
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    # Construct the rotation matrix
    rotation_matrix = np.array(
        [[cos_theta * scale, -sin_theta * scale, (1 - cos_theta) * center_x + sin_theta * center_y],
         [sin_theta * scale, cos_theta * scale, -sin_theta * center_x + (1 - cos_theta) * center_y]])

    return rotation_matrix


def rotate(image, angle):
    # Get the height and width of the image
    (h, w) = image.shape[:2]

    # Compute the center of the image
    center = (w // 2, h // 2)

    # Get the rotation matrix using cv2.getRotationMatrix2D function
    # you also can use 'get_rotation_matrix()' function
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Rotate the image using cv2.warpAffine function
    rotated = cv2.warpAffine(image, M, (w, h))

    # Return the rotated image
    return rotated


# Load the image using OpenCV
image = cv2.imread("HBD.JPG")

# Define the rotation angles
angles = [30, 60, 90, 120, 150, 180]

# Loop over the angles and points
for angle in angles:
    # Rotate the image clockwise
    rotated_clockwise = rotate(image, -angle)

    # Rotate the image counterclockwise
    rotated_counterclockwise = rotate(image, angle)

    # Show the rotated images side by side
    cv2.imshow(f"Rotated Clockwise {angle} degree", rotated_clockwise)
    cv2.imshow(f"Rotated Counterclockwise {angle} degree", rotated_counterclockwise)
    cv2.waitKey(0)

cv2.destroyAllWindows()
