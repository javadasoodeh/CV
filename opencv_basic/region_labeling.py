import cv2
import numpy as np

# Read input image
image = cv2.imread('HBD.jpg', 0)

# Threshold the image
ret, thresh = cv2.threshold(image, 92, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Threshold", thresh)

# Define a kernel for opening
kernel = np.ones((3, 3), np.uint8)

# Apply opening for removing noise and small text
binary_img = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
cv2.imshow("Binary Image - opening", binary_img)

# Perform connected component analysis
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_img)

# Print the returned values from connectedComponentsWithStats
print("Number of labels:", num_labels)
print("Labels matrix shape:", labels.shape)
print("Stats matrix shape:", stats.shape)
print("Centroids matrix shape:", centroids.shape)

# Access and print statistics for each labeled region
for label in range(1, num_labels):
    x, y, w, h, area = stats[label]
    print(f"Label: {label}")
    print(f" - Bounding box (x, y, w, h): ({x}, {y}, {w}, {h})")
    print(f" - Area: {area}")

# Create a random color map
colors = np.random.randint(0, 255, size=(num_labels, 3), dtype=np.uint8)

# Set background label to black
colors[0] = [0, 0, 0]

# Create output image
output = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)


# Color each region in the output image
for label in range(1, num_labels):
    output[labels == label] = colors[label]
    cv2.imshow('label {} added'.format(label), output)
    cv2.waitKey(0)

# Display the labeled image
cv2.imshow('Labeled Image', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
