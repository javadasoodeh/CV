import cv2
import argparse

# Set up the command-line argument parser
parser = argparse.ArgumentParser(description='Load and save an image using OpenCV')
parser.add_argument('--input_image', help='Path to the input image file', default='HBD.JPG')
parser.add_argument('--output_image', help='Path to the output image file', default='output_image.jpg')

# Parse the command-line arguments
args = parser.parse_args()

# Load the image using OpenCV
img = cv2.imread(args.input_image)

# Check if the image was loaded successfully
if img is None:
    print(f"Error: Could not open or read image file '{args.input_image}'.")
else:
    # Get the image dimensions
    height, width, channels = img.shape

    # Display the image dimensions
    print(f"Input image dimensions: {width} x {height} x {channels}")

    # Save the image to a new file
    cv2.imwrite(args.output_image, img)
    print(f"Image saved as '{args.output_image}'")
