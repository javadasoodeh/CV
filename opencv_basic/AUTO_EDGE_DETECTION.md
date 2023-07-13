# Introduction:
In image processing, the Canny edge detector is a popular algorithm for identifying the edges in an image. One of the main challenges with using the Canny edge detector is selecting appropriate threshold values for the lower and upper thresholds. Choosing the right values can be a time-consuming and iterative process, and it can be difficult to find the optimal values for a given image. In this tutorial, we will explore how to automatically select the threshold values for the Canny edge detector.

```python

# Automatically calculate lower and upper threshold values
v = np.median(blurred)
sigma = 0.33
lower_thresh = int(max(0, (1.0 - sigma) * v)))
upper_thresh = int(min(255, (1.0 + sigma) * v)))

```

The formula used to calculate the lower and upper threshold values for the Canny edge detection algorithm is based on statistical analysis of the image intensity values. The purpose of this calculation is to automatically determine the appropriate threshold values to distinguish edges from non-edges in the image.

The median value is used to calculate the threshold values because it is a measure of central tendency that is less sensitive to outliers than the mean. The median value represents the value at which half of the pixels in the image have a lower intensity value and half have a higher intensity value. By using the median value to calculate the threshold values, we can ensure that they are not affected by extreme pixel values that may occur due to noise or other factors.

The choice of sigma = 0.33 is a commonly used value in the Canny edge detection algorithm. This value is based on empirical observations and has been found to work well in practice. The purpose of sigma is to control the range of intensity values that are considered as edges. A higher value of sigma will result in a wider range of intensity values being considered as edges, while a lower value of sigma will result in a narrower range of intensity values being considered as edges.

The specific formula used to calculate the lower and upper threshold values is based on the assumption that the intensity values in the image follow a Gaussian distribution. The lower threshold value is calculated as (1.0 - sigma) * v, which represents the intensity value below which all pixels are considered non-edges. The upper threshold value is calculated as (1.0 + sigma) * v, which represents the intensity value above which all pixels are considered strong edges. The values are then clipped to ensure that they are within the valid range of intensity values (0 to 255 for an 8-bit image) and cast to integers.