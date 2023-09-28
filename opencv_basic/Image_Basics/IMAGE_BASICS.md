## Image Basics:

### Anatomy of Digital Images

The term "digital image" refers to a type of representation wherein a visual image is converted into a numerical format. 
This numerical representation can be manipulated, analyzed, and used in various applications using computer algorithms. 
So, Understanding its anatomy is crucial for anyone venturing into image processing. 
Here’s a deeper dive into the anatomy of digital images:


#### **Pixel**:

The fundamental unit of a digital image is a pixel, which stands for "picture element". 
A pixel represents the smallest controllable element of a picture represented on the screen. 
Each pixel corresponds to a specific position in an image and holds a value that determines its color.
In a grayscale image, the pixel value ranges from 0 to 255, where 0 represents black, 255 represents white, 
and values in between represent various shades of gray.

#### **Resolution**:

The resolution of an image refers to the total number of pixels contained in it. 
It is often represented as a pair of values — the number of rows and columns of pixels (e.g., 1920x1080). 
Higher resolution images have more details but are larger in file size.

#### **Channels**:
A channel in an image is a color scale such as Red, Green, or Blue. 
Most images use a combination of these three primary colors to represent a wide array of colors. 
A standard color image has three channels (RGB), while a grayscale image has just one channel.

In RGB images, each channel holds pixel values from 0 to 255, determining the intensity of the respective color. 

**Red Channel**: Represents the intensity of the red color.

**Green Channel**: Represents the intensity of the green color.

**Blue Channel**: Represents the intensity of the blue color.

The final color of each pixel is the combination of the values from all three channels.
For instance, pure red would be represented as (255, 0, 0), pure green as (0, 255, 0), and pure blue as (0, 0, 255).

#### **Color Depth / Bit Depth**:

Color depth, also known as bit depth, refers to the number of bits used to represent the color of a single pixel. 
An 8-bit depth per channel means each channel can have 256 different values ranging from 0 to 255.  
Therefore, an 8-bit depth RGB image can represent $256 × 256 × 256 = 16, 777, 216$ different colors.
By and large, a higher bit depth allows for a wider range of colors and smoother color transitions 
but at the cost of increased file size and processing requirements.

In a grayscale image with an 8-bit depth, there are 256 possible grayscale values. 
In contrast, a 16-bit depth grayscale image can have $2^16 = 65,536$ different shades of gray, 
offering more detail and subtler gradations of color.

#### Image Representation in Memory:

Digital images, once loaded into a computer, need to be stored in a way that can be easily accessed and manipulated. This is where the representation of images in memory comes into play.

- **Multi-dimensional Arrays**: Images are stored in computer memory as multi-dimensional arrays. In Python, this is typically achieved using NumPy arrays, which provide a convenient and efficient way to store and manipulate image data.
  
  - **Grayscale Images**: A grayscale image is represented as a 2D array, where each element corresponds to a pixel value. The values range from 0 to 255, representing varying shades of gray.
  
  - **Color Images**: A color image, on the other hand, is represented as a 3D array. Here, each pixel is represented by a 1D array of channel values. In the case of an RGB image, this 1D array would have three elements representing the red, green, and blue channel values respectively.

#### Metadata:

Apart from the visual data, digital images often carry additional information known as metadata. This data provides insight into various attributes of the image.

- **Intrinsic Information**: This includes details like the date and time the image was created, the camera settings used (such as aperture, shutter speed, and ISO level), the make and model of the camera, and much more. 

- **File Format Details**: Metadata also includes information about the file format, compression settings, and sometimes even a thumbnail of the image.

- **Geographical Information**: Some images, especially those taken with GPS-enabled devices, include geographical information indicating where the image was taken.

- **Copyright Information**: Copyright details, author information, and other related metadata can also be embedded within the image file.

Metadata can be invaluable when organizing, processing, or analyzing digital images. It's often accessed and managed using specialized libraries in Python.

### Image Formats: Lossless vs. Lossy

In this section, we delve into the fundamentals of image formats, primarily focusing on the distinction between lossless and lossy image formats. This knowledge is pivotal as it influences the quality and the usability of images in various applications.

#### Understanding Image Formats

Image formats are standards for organizing and storing digital images. Each format comes with its own set of specifications on how data is encoded and saved. The choice of format can impact the image's quality, file size, and compatibility with other software. Common image formats include JPEG, PNG, BMP, and TIFF.

#### Lossless Image Formats

Lossless image formats retain all the original quality of an image while saving or compressing. In lossless compression, no data is lost, and the original image can be perfectly reconstructed from the compressed image. This is crucial in scenarios where every detail in an image is vital, such as medical imaging or archival storage.

- **PNG (Portable Network Graphics)**: PNG is a popular lossless image format. It supports a wide range of color depths and also has support for transparency.
- **TIFF (Tagged Image File Format)**: TIFF is another lossless format widely used in professional environments and for storing high-quality images.
- **BMP (Bitmap)**: BMP is a basic, uncompressed lossless image format, which means the file size can be considerably larger compared to other formats.

#### Lossy Image Formats

Contrary to lossless formats, lossy image formats reduce file size by discarding some image information during compression. This results in a loss of image quality, which may or may not be noticeable depending on the extent of compression and the application at hand.

- **JPEG (Joint Photographic Experts Group)**: JPEG is a highly popular lossy image format. It achieves significant file size reduction by dropping image details, making it a preferred choice for web use.
- **WebP**: Developed by Google, WebP is a modern image format that provides superior compression for images on the web. It supports both lossless and lossy compression with good quality.

#### Choosing Between Lossless and Lossy

The choice between lossless and lossy image formats depends on the use case:

- **Quality Preservation**: If preserving image quality is paramount, a lossless format like PNG or TIFF is advisable.
- **File Size**: If reducing file size is a priority, especially for web use or storage considerations, a lossy format like JPEG may be suitable.

### Loading, displaying, and saving images 

In this section, we will explore how to load an image from a file, display it to the user, 
and then save it to a new file using OpenCV, a powerful library for image processing tasks.

<a href="/opencv_basic/Image_Basics/code/loading_displaying_and_saving.py"> code </a>

#### Loading Images with OpenCV

The process of loading images into a program is the first step in image processing. 
In this book, we will use the OpenCV library, which is a powerful tool for image and video processing. 
The function `cv2.imread()` is used to load an image from a file. Here is how it works:

```python
import cv2  # Import the OpenCV library

img = cv2.imread("../img/HBD.jpg")  # Load the image from file
```

- `cv2` is the module we import for using OpenCV functions.
- `cv2.imread()` is the function call to load the image, and the path to the image file is provided as an argument.

#### Understanding Image Dimensions

Images in OpenCV are represented as NumPy arrays. 
A color image is a 3D array, where the dimensions represent the image height, width, and color channels (usually Red, Green, and Blue).

```python
# Get the image dimensions
height, width, channels = img.shape

# Display the image dimensions
print(f"Input image dimensions: {width} x {height} x {channels}")
```

- `img.shape` returns the dimensions of the image as a tuple.
- The `height`, `width`, and `channels` are then unpacked from the tuple and printed to the console.

#### Displaying Images with OpenCV

Once the image is loaded, we can display it using the `cv2.imshow()` function, which creates a window to display the image.

```python
# Displaying the image
cv2.imshow("Image", img)
cv2.waitKey(0)  # Wait for a key press to close the window
```

- `cv2.imshow()` takes two arguments: the name of the window and the image object.
- `cv2.waitKey(0)` is a necessary line of code following `cv2.imshow()`. It waits for a key press to close the window. 
Without this line, the image window would close immediately. Its argument(delay) is optional and is in milliseconds. 
If omitted or zero, it waits indefinitely for a keystroke

#### Saving Images with OpenCV

After processing, we may want to save the new image to a file. We use `cv2.imwrite()` to do this:

```python
# Save the image to a new file
cv2.imwrite("output.jpg", img)
print("Image saved as output.jpg")
```

- `cv2.imwrite()` takes two arguments: the filename (including the desired path and extension) and the image object.
- This function returns `True` if the image is saved successfully and `False` otherwise.

#### output
Input image dimensions: 448 x 551 x 3

<p align="center">

<img src="/opencv_basic/Image_Basics/img/output-loading-displaying-and-saving.JPG" alt="output-loading-displaying-and-saving" width="550">

</p>
 
Image saved as output.jpg

### Accessing and Manipulating Pixels

In image processing, a pixel is the smallest addressable element in an image. Each pixel has a value representing 
its color, which, in a color image, is typically a triplet of red, green, and blue intensities (RGB).
In this section, we'll delve into the basics of how to access and manipulate pixels in an image using OpenCV in Python by a code snippet. 
We'll break down the code into smaller parts and explain each part thoroughly.

#### Importing Necessary Library

```python
import cv2
```

Here, we import the OpenCV library using the alias `cv2`. OpenCV is a vast library that provides a plethora of image 
and video processing functions.

#### Loading an Image

```python
# Load the image using OpenCV
image = cv2.imread("../img/HBD.jpg")
```

In this line, we use the `cv2.imread()` function to read the image file located at "../img/HBD.jpg" from 
the disk into memory. The image data is stored in a multi-dimensional NumPy array, `image`, 
where each element of the array corresponds to a pixel in the image.

#### Accessing a Specific Pixel

```python
# Get the value of a specific pixel
pixel_value = image[100, 100]
blue_value, green_value, red_value = pixel_value
print("Pixel value at (100, 100): Blue = {}, Green = {}, Red = {}".format(blue_value, green_value, red_value))
```

Here, we access the color value of the pixel at coordinates (100, 100) in the image. 
The coordinates are specified in the (row, column) format, which corresponds to the (y, x) position in the image. 
The `image[100, 100]` expression returns a NumPy array containing three values corresponding to 
the Blue, Green, and Red (BGR) color channels of the pixel. 

It's important to note that while we often think in RGB, OpenCV uses a BGR format.

We then unpack these values into individual variables `blue_value`, `green_value`, and `red_value` and print them out.

#### Setting the Value of a Specific Pixel

```python
# Set the value of a specific pixel
image[100, 100] = [255, 0, 0]  # set the pixel to blue
```

In this snippet, we set the color of the pixel at coordinates (100, 100) to blue. 
We specify the color as a list of BGR values, `[255, 0, 0]`. 
This is a straightforward way to modify a single pixel's color in an image.


#### Accessing a Range of Pixels

```python
# Get the values of a range of pixels
pixel_values = image[50:100, 50:100]
print("Pixel values in range (50-100, 50-100):")
for row in pixel_values:
    for pixel in row:
        blue_value, green_value, red_value = pixel
        print("Blue = {}, Green = {}, Red = {}".format(blue_value, green_value, red_value))
```

Here, we access a block of pixels in the image using the syntax `image[50:100, 50:100]`. 
This syntax uses Python's slicing mechanism to extract a rectangular region of the image 
from rows 50 to 99 and columns 50 to 99. The resulting `pixel_values` is a smaller image (or sub-image) 
extracted from the original image. We then iterate through each row and each pixel in those rows, 
printing out the BGR values of the pixels.

#### Setting the Values of a Range of Pixels

```python
# Set the values of a range of pixels
image[50:100, 50:100] = [0, 255, 0]  # set the pixels to green
```

Similar to how we accessed a range of pixels, we can also set the color values of a range of pixels. 
Here, we set all the pixels in the rectangular region from rows 50 to 99 and columns 50 to 99 to 
green (`[0, 255, 0]` in BGR).

#### Understanding the Image Shape

```python
# Get the shape of the image
height, width, channels = image.shape
print("Image shape: Height = {}, Width = {}, Channels = {}".format(height, width, channels))
```

The `image.shape` attribute returns a tuple representing the dimensions of the image. 
The tuple contains three values: the number of rows (height), the number of columns (width), 
and the number of color channels. This information is crucial when you need to loop through pixels or 
when you need to know the image dimensions for further processing.

#### Displaying the Modified Image

```python
# Show the modified image
cv2.imshow("Modified Image", image)
cv2.waitKey(0)
```

Finally, we use `cv2.imshow()` to display the modified image in a window titled "Modified Image". 
The `cv2.waitKey(0)` function waits indefinitely for a key press before closing the window. 
This gives you time to view the image.
