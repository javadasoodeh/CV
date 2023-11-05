## Image Manipulations and Transformations

### Image Arithmetic and Mathematical Operations

Image arithmetic and mathematical operations are fundamental tools in image processing. 
They allow us to manipulate the pixel values of an image, which can be crucial for various tasks
 such as enhancing the contrast of an image, isolating features of interest, or combining multiple images together.

In this section, we'll explore basic arithmetic operations like addition, subtraction, 
multiplication, and division, and we'll learn how to perform these operations 
using two popular libraries in Python: NumPy and OpenCV.

#### Importing Necessary Libraries

Firstly, let's import the necessary libraries. We'll be using OpenCV and NumPy for this section. 
OpenCV is a library specifically designed for computer vision tasks, 
while NumPy is a library for numerical operations in Python which is highly optimized for performance.

```python
import cv2
import numpy as np
```

#### Loading Images

We'll start by loading a grayscale image using OpenCV's `cv2.imread` function. 
The `cv2.IMREAD_GRAYSCALE` flag tells OpenCV to load the image in grayscale mode.

```python
# Load a grayscale image
image1 = cv2.imread('../img/HBD.jpg', cv2.IMREAD_GRAYSCALE)
```

Now, we'll create a second image with the same dimensions as `image1`, 
but with all pixel values set to 20. We use NumPy's `np.full_like` function for this, 
which creates an array of the same shape and type as a given array, filled with a specified value.

```python
# Create a second image with all values set to 20
image2 = np.full_like(image1, 20)
```

#### Arithmetic Operations using NumPy

Now, let's perform basic arithmetic operations on these images using NumPy. 
The `np.add`, `np.subtract`, `np.multiply`, and `np.divide` functions perform element-wise addition, 
subtraction, multiplication, and division respectively.

```python
# Perform arithmetic operations using NumPy
addition_numpy = np.add(image1, image2)
subtraction_numpy = np.subtract(image1, image2)
multiplication_numpy = np.multiply(image1, image2)
division_numpy = np.divide(image1, image2)
```

In these operations, each pixel value of `image1` is combined with the corresponding pixel value of `image2` 
using the specified operation. For example, in `np.add(image1, image2)`, 
the pixel value at position (0, 0) in `image1` is added to the pixel value at position (0, 0) in `image2`, 
and the result is stored in the corresponding position in `addition_numpy`. 
This is done for every pixel position in the images.

#### Arithmetic Operations using OpenCV

Now, let's perform the same arithmetic operations using OpenCV's functions. 
The `cv2.add`, `cv2.subtract`, `cv2.multiply`, and `cv2.divide` functions perform the same operations 
as their NumPy counterparts.

```python
# Perform arithmetic operations using OpenCV
addition_opencv = cv2.add(image1, image2)
subtraction_opencv = cv2.subtract(image1, image2)
multiplication_opencv = cv2.multiply(image1, image2)
division_opencv = cv2.divide(image1, image2)
```

One key difference is that OpenCV's functions handle saturation, 
which means that if a result of an operation is outside the valid range of values for the data type, 
it will be clipped to the nearest valid value. For example, if a pixel value in an 8-bit unsigned integer image is 250,
 and we add 10 to it, the result will be 255, not 260, since 255 is the maximum value allowed for this data type.
 
**On the other hand**, NumPy performs modulo arithmetic for integer overflow. So, in the same example, 
 adding $10$ to a pixel value of $250$ will result in a value of $4$ in NumPy, as $(250+10)mod256=4$.
 
To make NumPy behave similarly to OpenCV in terms of arithmetic operations, 
we can define functions for saturated arithmetic that ensure the results 
stay within the valid range of values for 8-bit unsigned integers (0 to 255). Here's how you can do it:

```python
def saturated_add(image1, image2):
    # Ensure the images have the same data type
    assert image1.dtype == image2.dtype, "Images must have the same data type"
    
    # Calculate the intermediate sum
    intermediate_sum = image1.astype(np.int16) + image2.astype(np.int16)
    
    # Clip the values to the range 0 to 255
    result = np.clip(intermediate_sum, 0, 255).astype(np.uint8)
    
    return result

def saturated_subtract(image1, image2):
    assert image1.dtype == image2.dtype, "Images must have the same data type"
    intermediate_diff = image1.astype(np.int16) - image2.astype(np.int16)
    result = np.clip(intermediate_diff, 0, 255).astype(np.uint8)
    return result

def saturated_multiply(image1, image2):
    assert image1.dtype == image2.dtype, "Images must have the same data type"
    intermediate_product = image1.astype(np.int16) * image2.astype(np.int16)
    result = np.clip(intermediate_product, 0, 255).astype(np.uint8)
    return result

def saturated_divide(image1, image2):
    assert image1.dtype == image2.dtype, "Images must have the same data type"
    # Avoid division by zero by adding a small constant
    intermediate_quotient = image1.astype(np.int16) / (image2.astype(np.int16) + 1e-7)
    result = np.clip(intermediate_quotient, 0, 255).astype(np.uint8)
    return result

# Perform saturated arithmetic operations using the defined functions
addition_numpy = saturated_add(image1, image2)
subtraction_numpy = saturated_subtract(image1, image2)
multiplication_numpy = saturated_multiply(image1, image2)
division_numpy = saturated_divide(image1, image2)
```

In the above code:
1. We defined four functions `saturated_add`, `saturated_subtract`, `saturated_multiply`, and `saturated_divide` to perform the arithmetic operations while ensuring the results are clipped to the range 0 to 255.
2. We temporarily converted the data type of the images to `np.int16` before performing the arithmetic operations to prevent wrapping of values.
3. We used `np.clip` to ensure that all values are within the valid range, and then converted the result back to `np.uint8` (8-bit unsigned integer).

Now, the results of these operations (`addition_numpy`, `subtraction_numpy`, `multiplication_numpy`, and `division_numpy`) should match the results obtained using OpenCV's functions (`addition_opencv`, `subtraction_opencv`, `multiplication_opencv`, and `division_opencv`).


#### Displaying the Images and Results

Now that we have performed the arithmetic operations, it's time to visualize the results. 
This will help us understand the impact of these operations on the images.

```python
# Display the images and arithmetic results
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.waitKey(0)
cv2.imshow('Addition (NumPy)', addition_numpy)
cv2.imshow('Addition (OpenCV)', addition_opencv)
cv2.waitKey(0)
cv2.imshow('Subtraction (NumPy)', subtraction_numpy)
cv2.imshow('Subtraction (OpenCV)', subtraction_opencv)
cv2.waitKey(0)
cv2.imshow('Multiplication (NumPy)', multiplication_numpy)
cv2.imshow('Multiplication (OpenCV)', multiplication_opencv)
cv2.waitKey(0)
cv2.imshow('Division (NumPy)', division_numpy)
cv2.imshow('Division (OpenCV)', division_opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

In the code snippet above, we use OpenCV's `cv2.imshow` function to display the original images and 
the results of the arithmetic operations. The `cv2.imshow` function creates a window and displays the image in it. 
The first argument to `cv2.imshow` is the name of the window, and the second argument is the image to be displayed.

The `cv2.waitKey(0)` function waits for a key press indefinitely, 
and once a key is pressed, it proceeds to the next line of code. 
This allows us to view each result individually before moving on to the next.

Finally, `cv2.destroyAllWindows` closes all OpenCV windows that were opened during the execution of the code.

Through this exercise, you'll notice how the arithmetic operations affect the images. 
Addition brightens the image, subtraction darkens it, multiplication can create a contrast effect, 
and division can invert the contrast.


### Bitwise Operations

#### Introduction
Bitwise operations are fundamental in digital image processing. They enable us to combine, manipulate, or extract specific parts of images based on their binary representations. In this section, we will use the OpenCV library, a powerful tool in computer vision, to perform these operations. While the operations are simple, they lay the foundation for more advanced image processing techniques.

#### Code Overview
For our demonstration, we'll create two simple binary images. These images will be represented as matrices with values of either 0 (black) or 255 (white). We'll then apply various bitwise operations on these matrices.

#### Code Breakdown

##### Importing the Libraries

```python
import cv2
import numpy as np
```

Here, we import two essential libraries:
- `cv2`: This is the OpenCV library which provides us with numerous computer vision functions.
- `numpy`: A library for numerical operations in Python. It's especially efficient for matrix and array operations, making it ideal for image processing.

##### Creating Binary Images

```python
image1 = np.zeros((300, 300), dtype=np.uint8)
image1[50:150, 100:200] = 255
```

`np.zeros((300, 300), dtype=np.uint8)`: This creates a 300x300 matrix filled with zeros. The `dtype=np.uint8` specifies that the values in the matrix are 8-bit unsigned integers (ranging from 0 to 255). This is a standard format for grayscale images.

`image1[50:150, 100:200] = 255`: This line uses array slicing to define a rectangle within the image and sets its pixel values to 255, making it white.

```python
image2 = np.zeros((300, 300), dtype=np.uint8)
image2[100:200, 150:250] = 255
```

Similarly, we create another binary image and define a different rectangular region as white.

##### Applying Bitwise Operations

```python
bitwise_and = cv2.bitwise_and(image1, image2)
bitwise_or = cv2.bitwise_or(image1, image2)
bitwise_xor = cv2.bitwise_xor(image1, image2)
bitwise_not = cv2.bitwise_not(image1)
```

The above code performs bitwise operations using OpenCV functions and returns a new image with the following conditions applied:
- `bitwise_and`: Sets a pixel to 255 (white) only if the corresponding pixels in both input images are 255.
- `bitwise_or`: Sets a pixel to 255 if at least one of the corresponding pixels in the input images is 255. 
- `bitwise_xor`:  If the corresponding pixels in the input images are the same (both white or both black), the output will be black (0).
 If one pixel is white (255) and the other is black (0), the output will be white (255).
- `bitwise_not`: Flips the pixel values of the input image (turns 0 to 255 and vice versa). 

##### Displaying the Results

```python
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Bitwise AND', bitwise_and)
cv2.imshow('Bitwise OR', bitwise_or)
cv2.imshow('Bitwise XOR', bitwise_xor)
cv2.imshow('Bitwise NOT', bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

`cv2.imshow()`: This function displays an image. It takes in two arguments: the name of the window and the image matrix.

`cv2.waitKey(0)`: Waits indefinitely for a key press. If you replace 0 with a number, it will wait for that many milliseconds.

`cv2.destroyAllWindows()`: Closes all OpenCV windows.

##### Detailed Explanation
The core of bitwise operations lies in binary logic. Let's understand this with a simple example. Consider two binary bits, A and B:

- Bitwise AND: $A \land B$ is 1 only if both A and B are 1.
- Bitwise OR: $A \lor B$ is 1 if at least one of A or B is 1.
- Bitwise XOR: $A \oplus B$ is 1 only if A or B is 1, but not both.
- Bitwise NOT: $\neg A$ inverts the value of A (1 becomes 0, 0 becomes 1).

When we perform these operations on images, we're applying these logics pixel by pixel. For instance, if two images have a white pixel (255) at the same location, the result of a bitwise AND operation at that location will also be a white pixel. If only one image has a white pixel at a location, the result of a bitwise OR operation at that location will be a white pixel.

By understanding and leveraging these basic bitwise operations, we can create masks, extract regions of interest, and implement various other image processing techniques in more advanced scenarios.

### Masking Techniques

## Introduction

Masking techniques in image processing allow us to focus on specific parts of an image, while ignoring the rest. This can be useful in various applications, such as object detection, where we want to isolate an object from the background. Essentially, a mask is a binary image that specifies which pixels of the original image are of interest: pixels where the mask is `1` (or `255` for an 8-bit image) are kept, while pixels where the mask is `0` are discarded.

## Code Overview

The provided code snippet demonstrates how to load an image using OpenCV, create a mask with a rectangular region of interest, apply this mask to the image, and then display the original, mask, and masked images. We will use OpenCV, a powerful library for image processing, and NumPy, a library for numerical operations in Python.

## Code Breakdown

Let's break down each part of the code:

```python
import cv2
import numpy as np
```

Here we import the required libraries:
- `cv2` is the OpenCV module for Python, used for image processing tasks.
- `numpy` is a library for numerical computations in Python, which OpenCV uses for handling images as arrays.

```python
image = cv2.imread('../img/HBD.jpg')
```

The `imread` function from the `cv2` module reads the image from the specified path and returns it as a NumPy array. If the image is in color, the default color space for OpenCV is BGR (Blue, Green, Red).

```python
mask = np.zeros(image.shape[:2], dtype=np.uint8)
```

We create a new NumPy array filled with zeros (black) with the same height and width as our original image. This will serve as our mask. The `dtype=np.uint8` argument specifies that each element in the array will be an 8-bit unsigned integer, which is the standard for images.

```python
roi = (80, 100, 360, 300)  # (x, y, width, height)
```

This line defines the region of interest (ROI) as a rectangle, with the top-left corner at (x=80, y=100) and dimensions of 360 pixels in width and 300 pixels in height.

```python
cv2.rectangle(mask, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), 255, -1)
```

Using OpenCV's `rectangle` function, we draw a rectangle on the mask. The first two arguments are the mask and the top-left corner of the rectangle. The third argument is the bottom-right corner, which we calculate by adding the width and height to the x and y coordinates, respectively. The fourth argument is the color (255, which is white for a binary image), and the fifth argument `-1` indicates that the rectangle should be filled completely.

```python
masked_image = cv2.bitwise_and(image, image, mask=mask)
```

Here we apply the mask to the image. The `bitwise_and` function performs a bitwise AND operation between the image and itself, using the mask to determine which pixels to keep. Only the pixels where the mask is white (255) are retained in the resulting `masked_image`.

```python
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

The `imshow` function is used to display the images in separate windows. `waitKey(0)` waits indefinitely for a key event, and `destroyAllWindows()` closes all the windows once a key is pressed.

## Detailed Explanation

When we apply the mask to the image with `bitwise_and`, it's like placing a sheet of paper with a hole cut out over the image. The hole in the paper (the white part of the mask) reveals the part of the image we are interested in, and the rest of the paper (the black part of the mask) covers the portions of the image we want to ignore.

The use of a mask is a very powerful technique because it allows for complex operations on specific parts of the image. For instance, we could perform color transformations, filtering, or feature detection solely within the region defined by the mask.

By understanding these fundamentals, you can start to explore more complex masking scenarios, such as irregular shapes, multiple regions of interest, and dynamic masks created through image processing techniques like thresholding and edge detection.
