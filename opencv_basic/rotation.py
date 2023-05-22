import cv2
import argparse
import math
import numpy as np


def get_rotation_matrix(center, angle, scale):
    # Convert the angle to radians
    theta = math.radians(angle)

    # Extract the center coordinates
    center_x, center_y = center

    # Calculate sine and cosine of the angle
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    # Construct the rotation matrix
    rotation_matrix = np.array([[cos_theta * scale, -sin_theta * scale, (1 - cos_theta) * center_x + sin_theta * center_y],
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


# Set up the command-line argument parser
parser = argparse.ArgumentParser(description='Load and save an image using OpenCV')
parser.add_argument('--input_image', help='Path to the input image file', default='HBD.JPG')

# Parse the command-line arguments
args = parser.parse_args()

# Load the image using OpenCV
image = cv2.imread(args.input_image)

# Define the rotation angles
angles = [30, 60, 90, 120, 150, 180]

# Loop over the angles and points
for angle in angles:

    # Rotate the image clockwise
    rotated_clockwise = rotate(image, -angle)

    # Rotate the image counterclockwise
    rotated_counterclockwise = rotate(image, angle)

    # Show the rotated images side by side
    cv2.imshow("Rotated Clockwise", rotated_clockwise)
    cv2.imshow("Rotated Counterclockwise", rotated_counterclockwise)
    cv2.waitKey(0)

cv2.destroyAllWindows()
