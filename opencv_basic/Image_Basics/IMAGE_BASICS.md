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
In color images, the representation is a bit more complex. 
A standard color image is composed of three channels: red, green, and blue (RGB). 
Each channel holds pixel values from 0 to 255, determining the intensity of the respective color. 
The final color of each pixel is the combination of the values from all three channels.

**Red Channel**: Represents the intensity of the red color.

**Green Channel**: Represents the intensity of the green color.

**Blue Channel**: Represents the intensity of the blue color.

The combination of these channels allows for the representation of millions of colors. 
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

####  **Image Representation in Memory**:
   - Images are stored in computer memory as multi-dimensional arrays. In Python, this is typically done using NumPy arrays.
   - A grayscale image is represented as a 2D array, where each element corresponds to a pixel value.
   - A color image is represented as a 3D array, where each pixel is represented by a 1D array of channel values.

#### **Metadata**:
   - Digital images often come with metadata, which is data about the image itself. This can include information like the date and time the image was created, the camera settings used, the file format, and much more.
