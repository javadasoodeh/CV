## Image Manipulations and Transformations

### Image Arithmetic and Mathematical Operations

Image arithmetic and mathematical operations are fundamental tools in image processing. 
They allow us to manipulate the pixel values of an image, which can be crucial for various tasks
 such as enhancing the contrast of an image, isolating features of interest, or combining multiple images together.

#### Code Overview 

In this section, we'll explore basic arithmetic operations like addition, subtraction, 
multiplication, and division, and we'll learn how to perform these operations 
using two popular libraries in Python: NumPy and OpenCV.

#### Code Breakdown

##### Importing Necessary Libraries

Firstly, let's import the necessary libraries. We'll be using OpenCV and NumPy for this section. 
OpenCV is a library specifically designed for computer vision tasks, 
while NumPy is a library for numerical operations in Python which is highly optimized for performance.

```python
import cv2
import numpy as np
```

##### Loading Images

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

##### Arithmetic Operations using NumPy

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

##### Arithmetic Operations using OpenCV

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
 
###### Saturated Arithmetic (Optional)
 
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


##### Displaying the Images and Results

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

In image processing, "masking" refers to the practice of defining a region of interest in an image and then performing operations only within that region. This technique is widely used in applications ranging from simple photo editing to complex computer vision tasks that require the identification and manipulation of specific parts of an image.

1. **Binary Masking**: Uses binary images (black and white) to define the regions of interest in the main image.
2. **Alpha Blending**: Involves using an alpha channel to blend images, controlling the transparency.
3. **Color-based Masking**: Selects parts of an image based on specific color ranges.
4. **Bitwise Operations**: Applies logical operations like AND, OR, XOR for masking.
5. **Geometric Masking**: Uses geometric shapes (circles, rectangles, polygons) to define regions for masking.
6. **Gradient Masks**: Creates masks based on gradient information, often used in edge detection.
7. **Thresholding**: Segregates regions of interest by thresholding pixel values.

For our introduction, we'll focus on the most straightforward approach, known as binary masking, which is the use of binary images to control the visibility of the main image.

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

Rotation is a fundamental transformation in image processing, involving changing the orientation of an image by a certain angle. This operation is crucial in various applications like aligning images taken from different angles, data augmentation in machine learning, or correcting the orientation of scanned documents.

Understanding rotation requires a grasp of basic geometry and linear algebra. When we rotate an image, we essentially move each pixel to a new location, following a circular path around a center point. The rotation angle determines how far each pixel moves along this path.

##### Code Overview
In the provided Python code, we use OpenCV to perform image rotation. The process involves:

1- Loading an image using OpenCV.  
2- Defining a list of angles for rotation.  
3- Creating a rotation matrix for each angle.  
4- Applying the rotation to the image using the rotation matrix.  
5- Displaying the rotated images.

##### Code Breakdown

###### Importing Libraries

```python
import cv2
import math
import numpy as np
```

- `cv2`: This is the OpenCV library, used for image processing tasks.
- `math`: A standard Python library for mathematical functions like `sin`, `cos`, and `radians`.
- `numpy`: A library for numerical computations in Python. It provides support for arrays (like matrices), which are crucial in image processing.

###### get_rotation_matrix Function

```python
def get_rotation_matrix(center, angle, scale):
    # Convert the angle to radians
    theta = math.radians(angle)

    # Extract the center coordinates
    center_x, center_y = center

    # Calculate sine and cosine of the angle
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    # Construct the rotation matrix
    rotation_matrix = np.array([[cos_theta * scale, -sin_theta * scale, (1 - cos_theta) * center_x + sin_theta * center_y],
                                [sin_theta * scale, cos_theta * scale, -sin_theta * center_x + (1 - cos_theta) * center_y]])

    return rotation_matrix
```

- **Function Purpose**: This function creates a rotation matrix. In image processing, a rotation matrix is used to rotate an image around a specific point (the center) by a specified angle.
- **Arguments**:
    - `center`: A tuple (x, y) representing the center of rotation.
    - `angle`: The angle in degrees by which the image is to be rotated.
    - `scale`: A scaling factor. If set to 1, the image size remains the same.
- **Conversion to Radians**: The angle is converted to radians (`theta = math.radians(angle)`) because trigonometric functions in Python's math module require angles in radians.
- **Trigonometry**: `cos_theta` and `sin_theta` represent the cosine and sine of the angle, respectively. They are fundamental in calculating the new positions of pixels after rotation.
- **Rotation Matrix Creation**: A 2x3 array is created using NumPy. This matrix is pivotal in determining how pixels in the original image are moved to new positions in the rotated image.

###### rotate Function
```python
def rotate(image, angle):
    # Get the height and width of the image
    (h, w) = image.shape[:2]

    # Compute the center of the image
    center = (w // 2, h // 2)

    # Get the rotation matrix using cv2.getRotationMatrix2D function
    # you also can use 'get_rotation_matrix()' function
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Rotate the image using cv2.warpAffine function
    rotated = cv2.warpAffine(image, M, (w, h))

    # Return the rotated image
    return rotated
```

- **Function Purpose**: This function rotates an image by a given angle.
- **Image Dimensions**: (`(h, w) = image.shape[:2]`) retrieves the height and width of the image. This is important for calculating the center of the image and for ensuring the rotated image has the same dimensions as the original.
- **Center of Rotation**: `center = (w // 2, h // 2)` calculates the center of the image. Rotation will occur around this point.
- **Rotation Matrix (OpenCV)**: `M = cv2.getRotationMatrix2D(center, angle, 1.0)` uses OpenCV's function to create a rotation matrix. This matrix is then used to transform the image's pixels to their new positions.
- **Applying Rotation**: `cv2.warpAffine(image, M, (w, h))` applies the rotation matrix to the image. This function handles the remapping of pixels from their original to new positions.

###### Main Execution Block

```python
# Load the image using OpenCV
image = cv2.imread("HBD.JPG")

# Define the rotation angles
angles = [30, 60, 90, 120, 150, 180]

# Loop over the angles and points
for angle in angles:

    # Rotate the image clockwise
    rotated_clockwise = rotate(image, -angle)

    # Rotate the image counterclockwise
    rotated_counterclockwise = rotate(image, angle)

    # Show the rotated images side by side
    cv2.imshow("Rotated Clockwise", rotated_clockwise)
    cv2.imshow("Rotated Counterclockwise", rotated_counterclockwise)
    cv2.waitKey(0)

cv2.destroyAllWindows()
```

- **Loading Image**: `cv2.imread("HBD.JPG")` loads an image from the specified file.
- **Rotation Angles**: A list of angles is defined to rotate the image by various degrees.
- **Applying Rotation**: For each angle, the image is rotated both clockwise and counterclockwise. This is achieved by using positive and negative angles, respectively.
- **Displaying Images**: `cv2.imshow()` displays the rotated images. `cv2.waitKey(0)` waits for a key press to proceed, and `cv2.destroyAllWindows()` closes the image windows.

##### Detailed Explanation

###### Understanding the Rotation Matrix
The rotation matrix is a fundamental concept in linear algebra used to rotate points in a plane. It is a 2x3 matrix for 2D image rotation, defined as:

$$
\begin{bmatrix}
\cos \theta & -\sin \theta & Tx \\\
\sin \theta & \cos \theta & Ty
\end{bmatrix}
$$

- $\theta$ is the rotation angle.
- $\cos \theta$ and $\sin \theta$ define the rotation part.
- $Tx$ and $Ty$ are translations applied after rotation, necessary to keep the image centered.

###### cv2.getRotationMatrix2D
This OpenCV function simplifies the creation of the rotation matrix. It requires the center of rotation, the rotation angle, and a scale factor (usually 1 for no scaling). 

###### cv2.warpAffine
This function applies the rotation matrix to the image. It maps the coordinates of the original image to the new coordinates after rotation. The function handles the interpolation and boundary issues that arise when pixels are moved.

###### Handling Image Boundaries
One challenge with rotation is that parts of the image might move outside the frame, getting clipped. To handle this, one can adjust the frame size or the center of rotation.

###### Mathematical Foundations
At the heart of rotation is the concept of coordinate transformation. Each pixel in the image is moved to a new location based on the rotation matrix. This operation is a combination of linear transformation (rotation) and translation. 
 
##### Deeper Dive into the Rotation Matrix Formula (Optional)

The formula for the rotation matrix in image processing is derived from the basic principles of linear algebra and geometry. Let's delve into the details of the formula:


test

$$  
rotationMatrix = \begin{bmatrix}
    \alpha & \beta & (1 - \alpha) \cdot center_x - \beta \cdot center_y \\\
    -\beta & \alpha & \beta \cdot center_x + (1 - \alpha) \cdot center_y  
\end{bmatrix}  
$$

where:
- $\alpha = \cos \theta  \times scale$
- $\beta = \sin \theta  \times scale$

###### Origin of the Formula

1. **Basic Rotation Matrix**: 
   - In 2D space, the basic rotation matrix for rotating a point $(x, y)$ around the origin (0,0) by an angle $\theta$ is given by:
     
$$ 
\begin{bmatrix} 
    \cos \theta & -\sin \theta \\\ 
    \sin \theta & \cos \theta 
\end{bmatrix} 
$$

     
   - This matrix rotates points around the origin. However, for images, we often need to rotate around the image's center or another point, not just the origin.

2. **Translation to Center**:
   - To rotate around a center point $(center_x, center_y)$, we first translate the image so that the center becomes the origin. This involves shifting every point by $-center_x$ and $-center_y$.

3. **Rotation and Re-translation**:
   - After translating the image, we apply the basic rotation matrix and then translate the image back. This additional translation is where the $(1 - \alpha)$ and $\beta$ terms in the formula come into play.

###### Breaking Down the Matrix

- **First Row $[ \alpha, \beta, (1 - \alpha) \cdot center_x - \beta \cdot center_y ]$**:
  - $\alpha$ and $\beta$ are responsible for the rotation.
  - $(1 - \alpha) \cdot center_x - \beta \cdot center_y$ adjusts the x-coordinate after rotation to ensure the rotation is around the center.

- **Second Row $[ -\beta, \alpha, \beta \cdot center_x + (1 - \alpha) \cdot center_y ]$**:
  - $-\beta$ and $\alpha$ also contribute to the rotation.
  - $\beta \cdot center_x + (1 - \alpha) \cdot center_y$ adjusts the y-coordinate similarly.

###### Understanding Scale
The `scale` factor is multiplied with $\cos \theta $ and $\sin \theta $ to allow for resizing of the image during rotation. A scale of 1 means the image size remains constant. 


##### Understanding the Rotation Matrix with Center Translation (Optional)

To delve deeper into the rotation matrix and how it incorporates translation to rotate an image around a specific point, let's revisit and expand upon the previous explanation with additional information.

###### Basic Concept of Rotation
In 2D space, the rotation of a point $(x, y)$ around the origin $(0, 0)$ by an angle $\theta$ changes its coordinates to $(x', y')$, calculated as:

$$
x' = x \cdot \cos \theta  - y \cdot \sin \theta  
$$

$$
y' = x \cdot \sin \theta  + y \cdot \cos \theta 
$$

###### Rotating Around an Arbitrary Center
When rotating around a different point, say $(center_x, center_y)$, we first translate the point so that $(center_x, center_y)$ becomes the origin. After rotation, we translate back. The equations for the new coordinates $(x', y')$ become:

$$
x' = (x - center_x) \cdot \cos \theta  - (y - center_y) \cdot \sin \theta  + center_x
$$

$$
y' = (x - center_x) \cdot \sin \theta  + (y - center_y) \cdot \cos \theta  + center_y
$$

###### Expansion and Rearrangement
Expanding and rearranging the terms for $x'$ and $y'$, we obtain:

$$
x' = x \cdot \cos \theta  - y \cdot \sin \theta  + (-\sin \theta  \cdot center_x + (1 - \cos \theta ) \cdot center_y) 
$$

$$
y' = x \cdot \sin \theta  + y \cdot \cos \theta  + (\cos \theta  \cdot center_x + \sin \theta  \cdot center_y - center_x)
$$

###### Rotation Matrix for Image Processing
Incorporating these into a 2x3 matrix for image processing, we get the rotation matrix:

$$ \begin{bmatrix} \cos \theta & -\sin \theta & -\sin \theta \cdot center_x + (1 - \cos \theta ) \cdot center_y \\\ \sin \theta & \cos \theta & \cos \theta \cdot center_x + \sin \theta \cdot center_y - center_y \end{bmatrix} $$

This matrix is used in OpenCV's `cv2.warpAffine` function to rotate the image around a specific point.

###### Understanding the Translation Component
- The terms $(- \sin \theta  \cdot center_x + (1 - \cos \theta ) \cdot center_y)$ and $(\cos \theta  \cdot center_x + \sin \theta  \cdot center_y - center_y)$ in the matrix are responsible for translating the image back after rotation around the new origin.
- They ensure that the rotation appears as if it's occurring around the specified center point, rather than the top-left corner of the image.

##### Deriving the Rotation Matrix Formulas Using Polar Coordinates (Optional)

To understand the rotation matrix formulas, we use polar coordinates and trigonometric sum of angle formulas. This approach provides a geometric understanding of the rotation process.

###### Polar Coordinates Representation

- Any point $(x, y)$ in a 2D plane can be represented in polar coordinates as $(r \cos \phi, r \sin \phi)$, where $r$ is the radius (distance from the origin) and $\phi$ is the angle with the positive x-axis.
- $x = r \cos \phi$ and $y = r \sin \phi$.

![proof](/opencv_basic/Image_Manipulations_and_Transformations/img/rotate5.png)

###### Rotating the Point

- When rotating this point by an angle $\theta$, the radius $r$ remains the same, but the angle $\phi$ increases by $\theta$.
- The new coordinates $(x', y')$ after rotation are:
  - $x' = r \cos(\phi + \theta)$
  - $y' = r \sin(\phi + \theta)$

###### Applying Sum of Angle Formulas

- Using sum of angle formulas:
  - $\cos(\phi + \theta) = \cos \phi \cos \theta - \sin \phi \sin \theta$
  - $\sin(\phi + \theta) = \sin \phi \cos \theta + \cos \phi \sin \theta$
- Substituting these, we get:
  - $x' = r \cos \phi \cos \theta - r \sin \phi \sin \theta$
  - $y' = r \sin \phi \cos \theta + r \cos \phi \sin \theta$

###### Expressing in Cartesian Coordinates

- Recall $x = r \cos \phi$ and $y = r \sin \phi$, then:
  - $x' = x \cos \theta - y \sin \theta$
  - $y' = y \cos \theta + x \sin \theta$

###### Matrix Formulation

- These equations in matrix form:

$$ \begin{bmatrix} x' \\\ y' \end{bmatrix} = \begin{bmatrix} \cos \theta & -\sin \theta \\\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\\ y \end{bmatrix} $$

- This is the rotation matrix, which rotates a point $(x, y)$ by $\theta$ counterclockwise.


#### Cropping

Cropping is a fundamental technique in image processing and computer vision. It refers to the process of extracting a subregion of an image, often to focus on a particular area or to remove unwanted parts. Cropping is widely used in various applications like photo editing, object detection, and feature extraction.

In this section, we'll explore how to perform cropping using Python and OpenCV. 

##### Code Overview
The provided code demonstrates how to crop an image using OpenCV in Python. It involves these key steps:
1. Importing OpenCV.
2. Defining a function to crop the image.
3. Specifying the crop region.
4. Displaying the cropped image.

##### Code Breakdown
Let's delve into each part of the code for a comprehensive understanding.

1. **Importing OpenCV**:
   ```python
   import cv2
   ```
   - `cv2` is the Python interface for OpenCV. Importing it enables access to all the functions and classes required for image processing tasks.

2. **Defining the Crop Function**:
   ```python
   def crop_image(image_path, x, y, width, height):
       # Load the image
       image = cv2.imread(image_path)

       # Crop the image / numpy array slicing
       cropped_image = image[y:y + height, x:x + width]

       return cropped_image
   ```
   - `crop_image` is a user-defined function to handle the cropping operation.
   - `cv2.imread(image_path)`: This line reads the image from the specified path into a NumPy array. The array represents pixel intensities in the image.
   - `cropped_image = image[y:y + height, x:x + width]`: Here, array slicing is used to select a specific region of the image. The slicing `[y:y + height, x:x + width]` extracts the pixels in the rectangular region defined by the coordinates `(x, y)` and the specified `width` and `height`.

3. **Specifying the Crop Region**:
   ```python
   image_path = "HBD.jpg"
   x = 80
   y = 130
   width = 280
   height = 120
   ```
   - `image_path`: Path to the image file.
   - `x, y`: Coordinates of the top-left corner of the crop region.
   - `width, height`: Dimensions of the crop region.

4. **Displaying the Cropped Image**:
   ```python
   cropped_img = crop_image(image_path, x, y, width, height)
   cv2.imshow("Cropped Image", cropped_img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```
   - `crop_image(...)`: This line calls the crop function with the specified parameters.
   - `cv2.imshow(...)`: Opens a window to display the cropped image.
   - `cv2.waitKey(0)`: Waits for a key press to proceed.
   - `cv2.destroyAllWindows()`: Closes all OpenCV windows opened by the script.

##### Detailed Explanation

###### Image Representation in OpenCV
- OpenCV reads images into a NumPy array, which is essentially a grid of pixel values.
- For a color image, this array is 3-dimensional, with each pixel having three components (Red, Green, Blue).

###### Array Slicing for Cropping
- Array slicing is a feature in NumPy that allows for selecting a subset of an array. 
- `image[y:y + height, x:x + width]` selects a rectangular region from the image. The first part `y:y + height` selects the rows (vertical range), and `x:x + width` selects the columns (horizontal range).

###### Pixel Coordinates
- In the NumPy array (image), coordinates are represented as rows and columns.
- `(0, 0)` is typically the top-left corner of the image, with `x` increasing to the right and `y` increasing downward.

###### Cropping and Memory Efficiency
- The cropping operation in this code does not copy the selected region; it merely creates a view into the original array. This makes cropping very memory efficient in Python and OpenCV.

#### Flipping

Flipping is another fundamental image processing technique that mirrors an image along a specified axis. It's used in various applications like data augmentation, image correction, and artistic effects. Flipping can be horizontal, vertical, or both, altering the image's orientation and perspective.

##### Code Overview

To demonstrate flipping using OpenCV in Python, we will:
1. Load an image.
2. Perform horizontal, vertical, and both-axis flipping.
3. Display the original and flipped images.

##### Code Breakdown

###### Importing OpenCV

```python

import cv2

```

OpenCV is a library aimed at real-time computer vision, providing tools for image processing and computer vision tasks.

###### The `flip_image` Function

```python
def flip_image(image, direction):
```

This function takes two arguments: `image` (the image data) and `direction` (the flipping direction).

###### Flipping Directions

The `cv2.flip` function is used based on the `direction` argument:

```python
if direction == 'horizontal':
    flipped_image = cv2.flip(image, 1)
elif direction == 'vertical':
    flipped_image = cv2.flip(image, 0)
elif direction == 'both':
    flipped_image = cv2.flip(image, -1)
```

###### Loading the Image

```python
image_path = 'HBD.jpg'  # Replace with your image path
image = cv2.imread(image_path)
```

We use `cv2.imread` to load the image into an array of pixel values.

###### Applying the Flipping

We apply the `flip_image` function to the loaded image in different directions and display the results using `cv2.imshow`.

##### Detailed Explanation

To understand the mathematics behind flipping, let's consider a 2D image represented by a matrix or an array. Each pixel in the image can be addressed by its row and column indices. The top-left pixel corresponds to (0, 0), and the bottom-right pixel to (rows-1, cols-1), where 'rows' and 'cols' represent the number of rows and columns in the image, respectively.

When flipping an image, we reflect the pixels along a certain axis:

- **flipCode = 0: Vertical flipping**
  - Reflects the image pixels vertically, flipping it upside down.
  
  - Mathematically: $newRow = (	rows - 1) - 	currentRow, 	newCol = 	currentCol$
  
  
- **flipCode > 0: Horizontal flipping**
  - Reflects the image pixels horizontally, flipping it from left to right.
  - Mathematically: $newRow = 	currentRow, 	newCol = (	cols - 1) - 	currentCol$


- **flipCode < 0: Both directions**
  - Reflects the image pixels horizontally and vertically.
  - Mathematically: $newRow = (	rows - 1) - 	currentRow, 	newCol = (	cols - 1) - 	currentCol$


By applying these transformations to each pixel, the `cv2.flip()` function flips the image as specified. OpenCV optimizes this operation using efficient matrix operations, leveraging hardware acceleration and internal optimizations.


#### Resizing

##### Interpolation Methods: Advantages and Disadvantages

Here is an overview of the advantages and disadvantages of each interpolation method:

- cv2.INTER_NEAREST: Fastest method, but can result in pixelation and loss of image quality.
- cv2.INTER_LINEAR: Produces smooth results, but may introduce blurring in certain cases.
- cv2.INTER_CUBIC: Provides higher quality than linear interpolation but is slower.
- cv2.INTER_LANCZOS4: Generates sharp and high-quality results but requires more computational resources.
- cv2.INTER_AREA: Suitable for downsampling images, preserving details, and reducing aliasing artifacts.
- cv2.INTER_LINEAR_EXACT: Bit exact bilinear interpolation, providing the highest accuracy but at a higher computational cost.

Each method has its own strengths and weaknesses, and the choice depends on the specific requirements of 
your application, such as the desired trade-off between speed and image quality, the nature of the image, 
and the computational resources available.
