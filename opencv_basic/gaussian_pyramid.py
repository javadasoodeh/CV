import cv2


def generate_gaussian_pyramid(image, levels):
    pyramid = [image]
    for i in range(levels - 1):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid


def display_pyramid(pyramid):
    for i, image in enumerate(pyramid):
        cv2.imshow(f"Level {i + 1}", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Load the image
image = cv2.imread('HBD.jpg')

# Specify the number of pyramid levels
levels = 4

# Generate the Gaussian pyramid
pyramid = generate_gaussian_pyramid(image, levels)

# Display the pyramid
display_pyramid(pyramid)
