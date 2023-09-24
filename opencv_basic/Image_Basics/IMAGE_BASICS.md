### Image Basics:

#### Anatomy of Digital Images

A digital image is essentially a numerical representation of a visual image. Understanding its anatomy is crucial for anyone venturing into image processing. Here are the key components:

1. **Pixel**:
   - A pixel (short for "picture element") is the basic unit of a digital image. Each pixel represents a single point in the image.
   - Pixels are arranged in a grid, forming a two-dimensional array of rows and columns. The dimensions of this grid determine the image's resolution (e.g., 1920x1080 pixels).

2. **Channels**:
   - Each pixel can have one or more values associated with it, representing different color channels.
   - In a grayscale image, each pixel has one value representing its intensity, ranging from 0 (black) to 255 (white).
   - In a color image, typically, each pixel has three values corresponding to the Red, Green, and Blue (RGB) channels. Each channel value usually ranges from 0 to 255, allowing for over 16 million possible colors per pixel.

3. **Bit Depth**:
   - Bit depth refers to the number of bits used to represent each pixel's color information. Common bit depths include 8-bit (256 levels), 16-bit (65,536 levels), and 24-bit (16.7 million colors) per channel.
   - Higher bit depth allows for a wider range of colors and smoother color transitions but at the cost of increased file size and processing requirements.

4. **Image Representation in Memory**:
   - Images are stored in computer memory as multi-dimensional arrays. In Python, this is typically done using NumPy arrays.
   - A grayscale image is represented as a 2D array, where each element corresponds to a pixel value.
   - A color image is represented as a 3D array, where each pixel is represented by a 1D array of channel values.

5. **Metadata**:
   - Digital images often come with metadata, which is data about the image itself. This can include information like the date and time the image was created, the camera settings used, the file format, and much more.

6. **Image File Formats**:
   - Digital images can be saved in various file formats, each with its own set of features. Common formats include JPEG, PNG, BMP, and TIFF.
   - Some formats are lossless, preserving the exact pixel values, while others are lossy, compressing the image data to reduce file size at the cost of image quality.
