import cv2
import numpy as np

# Load the main image and the template image
main_image = cv2.imread('foreground.jpg')
template = cv2.imread('background.jpg')

# Convert the template image to grayscale
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# Perform template matching
result = cv2.matchTemplate(main_image, template_gray, cv2.TM_CCOEFF_NORMED)

# Find the location of the best match
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
top_left = max_loc
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])

# Draw a rectangle around the best match
cv2.rectangle(main_image, top_left, bottom_right, (0, 255, 0), 2)

# Display the result
cv2.imshow('Template Matching Result', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
