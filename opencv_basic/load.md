Load and Save an Image using OpenCV in Python
This tutorial shows how to load and save an image in Python using the OpenCV library. OpenCV is a popular computer vision library that can be used for various image and video processing tasks. We will be using the argparse module to allow the user to input the image file path as a command-line argument.

Prerequisites
Before starting, make sure you have the following prerequisites:

Python 3.x installed on your system
OpenCV-Python library installed on your system
Basic knowledge of Python programming
Steps
Importing Required Libraries
Setting up the Command-Line Argument Parser
Parsing the Command-Line Arguments
Loading the Image
Getting the Image Dimensions
Displaying the Image Dimensions
Saving the Image
Code Explanation
A detailed explanation of the code is provided in the load.py file.

How to Run the Code
Clone this repository
Navigate to the repository directory
Run the following command to load and save the default image:
Copy
python load.py
To load and save a custom image, run the following command:
Copy
python load.py --input_image <path_to_input_image> --output_image <path_to_output_image>
Replace <path_to_input_image> and <path_to_output_image> with the actual file paths.

Conclusion
This tutorial provided a basic introduction to loading and saving an image using OpenCV in Python. It also demonstrated how to use the argparse module to accept command-line arguments for input and output image file paths.