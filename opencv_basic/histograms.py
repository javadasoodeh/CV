import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 3: Load the image
image_path = 'HBD.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)

# Step 4: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 5: Calculate the histogram
hist, bins = np.histogram(gray_image.flatten(), 256, [0, 256])

# Step 6: Plot the histogram
plt.plot(hist, color='gray')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.title('Grayscale Image Histogram')
plt.show()

# Step 7: Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
