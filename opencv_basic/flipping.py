import cv2


def flip_image(image, direction):
    if direction == 'horizontal':
        flipped_image = cv2.flip(image, 1)
    elif direction == 'vertical':
        flipped_image = cv2.flip(image, 0)
    elif direction == 'both':
        flipped_image = cv2.flip(image, -1)
    else:
        print("Invalid direction! Please choose 'horizontal', 'vertical', or 'both'.")
        return None
    return flipped_image


# Load the image
image_path = 'HBD.jpg'  # Replace with your image path
image = cv2.imread(image_path)

# Flip the image horizontally
horizontal_flip = flip_image(image, 'horizontal')

# Flip the image vertically
vertical_flip = flip_image(image, 'vertical')

# Flip the image both horizontally and vertically
both_flip = flip_image(image, 'both')

# Display the original and flipped images
cv2.imshow('Original Image', image)
cv2.imshow('Horizontal Flip', horizontal_flip)
cv2.imshow('Vertical Flip', vertical_flip)
cv2.imshow('Both Flip', both_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
