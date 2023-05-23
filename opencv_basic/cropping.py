import cv2


def crop_image(image_path, x, y, width, height):
    # Load the image
    image = cv2.imread(image_path)

    # Crop the image / numpy array slicing
    cropped_image = image[y:y + height, x:x + width]

    return cropped_image


# Specify the image path
image_path = "HBD.jpg"

# Specify the region of interest for cropping
x = 80  # x-coordinate of the top-left corner
y = 130  # y-coordinate of the top-left corner
width = 280  # Width of the region
height = 120  # Height of the region

# Call the crop_image function
croped_img = crop_image(image_path, x, y, width, height)

# Display the cropped image
cv2.imshow("Cropped Image", croped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
