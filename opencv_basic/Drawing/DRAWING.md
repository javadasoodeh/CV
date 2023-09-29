## Drawing Lines, Rectangles, Square, and Circles
Drawing shapes on images is a fundamental aspect of image processing which aids in understanding 
the image coordinate system, color representation, and manipulation of image data.
In this section will explore a code snippet for drawing geometric shapes on images using OpenCV.
<a href="opencv_basic/Drawing/code/drawing_lines_rectangles_square_and_circles.py"> Here is the complete Code! </a>  


### Importing Libraries

Firstly, we need to import the necessary libraries:

```python
import cv2
import numpy as np
```

- `cv2` is the OpenCV library, a powerful open-source library for image processing and computer vision tasks.
- `numpy` is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

### Creating a Blank Image

We start by creating a blank image to draw shapes on. In OpenCV, images are represented as NumPy arrays with dimensions \([height, width, channels]\), where \(channels\) corresponds to the color channels of the image.

```python
# Create a black image with dimensions 300x400 and 3 channels
height, width = 300, 400
channels = 3
image = np.zeros((height, width, channels), dtype=np.uint8)
```

- `np.zeros()` is a function from the NumPy library which creates an array filled with zeros. The shape of the array is specified by the argument \((height, width, channels)\), and `dtype=np.uint8` specifies that the data type of the elements in the array should be 8-bit unsigned integer, which is the standard for image data.

### Drawing a Line

Drawing a line is one of the simplest drawing operations you can perform on an image. The `cv2.line()` function is used for this purpose.

```python
# Draw a line
start_point = (0, 0)
end_point = (width, height)
color = (0, 0, 255)  # Red color in BGR
thickness = 2
cv2.line(image, start_point, end_point, color, thickness)
```

- `start_point` and `end_point` are tuples representing the coordinates of the start and end points of the line, respectively.
- `color` is a tuple representing the color of the line in BGR (Blue, Green, Red) format.
- `thickness` is an integer value representing the thickness of the line in pixels.

### Drawing a Rectangle

To draw a rectangle on an image, we use the `cv2.rectangle()` function. This function requires the coordinates of the top-left corner and the bottom-right corner of the rectangle.

```python
# Draw a rectangle
top_left = (50, 50)
bottom_right = (150, 150)
color = (0, 255, 0)  # Green color in BGR
thickness = 3
cv2.rectangle(image, top_left, bottom_right, color, thickness)
```

- `top_left` and `bottom_right` are tuples representing the coordinates of the top-left and bottom-right corners of the rectangle, respectively.
- The `color` and `thickness` parameters serve the same purpose as they did in the `cv2.line()` function.

### Drawing a Square

Drawing a square is a specific case of drawing a rectangle where all sides are of equal length. 

```python
# Draw a square
top_left = (200, 50)
side_length = 50
color = (255, 0, 0)  # Blue color in BGR
thickness = -1  # Filled square
bottom_right = (top_left[0] + side_length, top_left[1] + side_length)
cv2.rectangle(image, top_left, bottom_right, color, thickness)
```

- In this case, we calculate the `bottom_right` corner based on the `top_left` corner and the `side_length`.
- Setting `thickness` to -1 instructs OpenCV to draw a filled rectangle.

### Drawing Circles

To draw circles, we use the `cv2.circle()` function.

```python
# Create 10 random circles
for i in range(10):
    center = (np.random.randint(0, width), np.random.randint(0, height))
    radius = np.random.randint(10, 50)
    color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))  # Random color in BGR
    thickness = -1  # Filled circle
    cv2.circle(image, center, radius, color, thickness)
```

- `center` is a tuple representing the coordinates of the center of the circle.
- `radius` is an integer value representing the radius of the circle in pixels.
- Again, the `color` and `thickness` parameters serve the same purpose as before.

### Displaying the Image

Finally, we use the `cv2.imshow()` and `cv2.waitKey()` functions to display the image and wait for a key press to close the window.

```python
# Show the image
cv2.imshow("Shapes", image)
cv2.waitKey(0)
```

- `cv2.imshow()` creates a window to display the image, with "Shapes" being the title of the window.
- `cv2.waitKey(0)` waits indefinitely for a key press before closing the window and ending the program.

### Output

<p align="center">

<img src="opencv_basic/Drawing/img/output-drawing-lines-rectangles-square-and-circles.JPG" alt="ooutput-drawing-lines-rectangles-square-and-circles" width="550">

</p>