## Image Manipulations and Transformations
\# change the style (introduction, code, ...)
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

#### Detailed Explanation
The core of bitwise operations lies in binary logic. Let's understand this with a simple example. Consider two binary bits, A and B:

- Bitwise AND: $A \land B$ is 1 only if both A and B are 1.
- Bitwise OR: $A \lor B$ is 1 if at least one of A or B is 1.
- Bitwise XOR: $A \oplus B$ is 1 only if A or B is 1, but not both.
- Bitwise NOT: $\neg A$ inverts the value of A (1 becomes 0, 0 becomes 1).

When we perform these operations on images, we're applying these logics pixel by pixel. For instance, if two images have a white pixel (255) at the same location, the result of a bitwise AND operation at that location will also be a white pixel. If only one image has a white pixel at a location, the result of a bitwise OR operation at that location will be a white pixel.

By understanding and leveraging these basic bitwise operations, we can create masks, extract regions of interest, and implement various other image processing techniques in more advanced scenarios.

### Masking Techniques

#### Introduction

In image processing, "masking" refers to the practice of defining a region of interest in an image and then performing operations only within that region. This technique is widely used in applications ranging from simple photo editing to complex computer vision tasks that require the identification and manipulation of specific parts of an image.

When we talk about "techniques," we mean the various ways in which masking can be implemented. For our introduction, we'll focus on the most straightforward approach, known as binary masking, which is the use of binary images to control the visibility of the main image.

#### Code Overview
We will go through the following process in our code:
1. Load an image into our program.
2. Define a binary mask, which is an array of zeros and ones where ones (or in our case, 255s) indicate the area of interest.
3. Apply this mask to the original image so that only the area of interest is visible.
4. Display the original image, the binary mask, and the masked image.

#### Code Breakdown
Let's explain each part of the code in detail.

##### Importing Libraries

```python
import cv2
import numpy as np
```

- `import cv2`: This line imports the OpenCV library into our Python script. OpenCV is a large library that provides tools for image and video processing. The "cv" in "cv2" stands for "computer vision."
- `import numpy as np`: This imports the NumPy library and gives it the alias "np" for convenience. NumPy is a fundamental package for scientific computing in Python. It provides a high-performance multidimensional array object, which is a powerful data structure for representing images as grids of pixels.

##### Loading the Image

```python
image = cv2.imread('../img/HBD.jpg')
```
- `cv2.imread()`: This function reads an image from the specified file. The argument `'../img/HBD.jpg'` is the file path to the image you want to load. It returns the image as a NumPy array, with the color channels in the order Blue-Green-Red (BGR).

##### Creating the Mask
```python
mask = np.zeros(image.shape[:2], dtype=np.uint8)

roi = (80, 100, 360, 300)  # (x, y, width, height)

cv2.rectangle(mask, (roi[0], roi[1]), (roi[0] + roi[2], roi[1] + roi[3]), 255, -1)
```
- `np.zeros()`: This function creates a new array, filled with zeros. The `image.shape[:2]` part retrieves the dimensions of the loaded image (height and width) but excludes the color channels. The result is a two-dimensional array (or grid) the same size as the image but only one layer deep, as we are creating a mask in grayscale.
- `dtype=np.uint8`: This specifies that the array should be made up of 8-bit unsigned integers, which is the standard for images (ranges from 0 to 255).
- `roi = (80, 100, 360, 300)`: This is a tuple defining the region of interest in the image. The numbers represent the top-left corner's x and y coordinates, and the width and height of the rectangle.
- `cv2.rectangle()`: This function draws a rectangle on the mask. The first two arguments are the x and y coordinates of the top-left corner of the rectangle. The next two arguments are the x and y coordinates of the bottom-right corner. The color `255` is used to fill the rectangle, and `-1` indicates that the rectangle should be filled completely.

##### Applying the Mask
```python
masked_image = cv2.bitwise_and(image, image, mask=mask)
```
- `cv2.bitwise_and()`: This function applies a bitwise AND operation to the pixels of two images. The AND operation is performed between each corresponding pixel of the two images. However, because we have provided the same image as both the first and second arguments, the operation is effectively just applied to one image. The third argument, `mask=mask`, tells the function to only perform the operation where the mask has white pixels (value 255).

##### Displaying the Images
```python
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Masked Image', masked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- `cv2.imshow()`: This function creates a window that displays an image. The first argument is the name of the window, and the second argument is the image to display.
- `cv2.waitKey(0)`: This function waits for a key press. The `0` argument means it will wait indefinitely until a key is pressed.
- `cv2.destroyAllWindows()`: This function closes all of the windows that were opened by the `imshow` function.

#### Detailed Explanation

In the context of binary masking, the mask tells the computer which pixels of the original image should be kept and which should be discarded. When the `bitwise_and` operation is applied with the mask, pixels aligned with the white part of the mask are kept, while all others are set to black, effectively "masking" them out.

This is an essential technique in image processing, as it allows us to focus on specific parts of an image and perform operations only on those parts. It lays the foundation for more advanced operations such as background subtraction, object isolation, and region-based processing.


### Spatial Operations: Translation, Rotation, Resizing, Flipping, Cropping

In this section, we will delve into the foundational concepts of spatial operations in image processing, 
focusing on translation, rotation, resizing, flipping, and cropping. These operations are essential for 
manipulating the spatial arrangement of pixels in an image and are fundamental to 
various tasks in computer vision.


#### Rotation

Rotation involves changing the orientation of an image by a certain angle. This operation is crucial in various applications like aligning images taken from different angles, data augmentation in machine learning, or correcting the orientation of scanned documents.

Understanding rotation requires a grasp of basic geometry and linear algebra. When we rotate an image, we essentially move each pixel to a new location, following a circular path around a center point. The rotation angle determines how far each pixel moves along this path.

##### Code Overview
In the provided Python code, we use OpenCV to perform image rotation. The process involves:

1- Loading an image using OpenCV.
2- Defining a list of angles for rotation.
3- Creating a rotation matrix for each angle.
4- Applying the rotation to the image using the rotation matrix.
5- Displaying the rotated images.

