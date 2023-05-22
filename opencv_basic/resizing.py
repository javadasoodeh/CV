import cv2


def resize_image(image, new_width, interpolation_method):
    # Get the current dimensions of the image
    (height, width) = image.shape[:2]

    # Calculate the ratio of the new width to the original width
    ratio = new_width / width

    # Calculate the new height using the aspect ratio
    new_height = int(height * ratio)

    # Resize the image using the specified interpolation method
    resized_image = cv2.resize(image, (new_width, new_height), interpolation=interpolation_method)

    return resized_image


# Load the image using OpenCV
image = cv2.imread('HBD.JPG')

# Define the desired new width
new_width = 600

# Specify the interpolation methods to use
interpolation_methods = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4, cv2.INTER_AREA,
                         cv2.INTER_LINEAR_EXACT]

# Loop over the interpolation methods
for interpolation_method in interpolation_methods:
    # Resize the image using the current interpolation method
    resized_image = resize_image(image, new_width, interpolation_method)

    # Display the resized image
    cv2.imshow(f"Resized Image - {interpolation_method}", resized_image)
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
