import cv2
import numpy as np

# loading image
image = cv2.imread('../img/HBD.JPG')

# Define the vertices of a polygon (here a triangle)
pts = np.array([[5, 150], [100, 75], [5, 10]], dtype=np.int32)

# Draw the polygon
isClosed = True  # This flag indicates whether the polygon is closed or not
color = (255, 0, 0)  # Blue color in BGR
thickness = 2  # Thickness of the line

cv2.polylines(image, [pts], isClosed, color, thickness)


# Set the font, scale, color, and thickness
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
fontColor = (0, 255, 0)  # White color
lineType = 2

# Set the position
position = (110, 85)

# Draw the text
cv2.putText(image, 'Triangle', position, font, fontScale, fontColor, lineType)

# Show the image
cv2.imshow("Polygon & Text", image)
cv2.waitKey(0)
