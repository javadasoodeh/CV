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
 
 On the other hand, NumPy performs modulo arithmetic for integer overflow. So, in the same example, 
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





 