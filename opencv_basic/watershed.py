import cv2
import numpy as np
import matplotlib.pyplot as plt

def watershed_segmentation(image_path):
    # Read the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Apply thresholding to obtain a binary image
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Perform morphological operations to remove noise
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # Perform a dilation operation to close gaps in between object edges
    sure_bg = cv2.dilate(opening, kernel, iterations=3)

    # Compute the distance transform
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

    # Threshold the distance transform to obtain a foreground region
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Subtract the foreground region from the background region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    # Mark the unknown region with 0
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    # Apply the Watershed algorithm
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]  # Mark the boundaries with blue color

    # Plot the segmented image
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].imshow(image)
    ax[0].set_title('Original Image')
    ax[0].axis('off')
    ax[1].imshow(markers, cmap='nipy_spectral')
    ax[1].set_title('Segmented Image')
    ax[1].axis('off')
    plt.show()

# Example usage
image_path = 'HBD.jpg'
watershed_segmentation(image_path)
