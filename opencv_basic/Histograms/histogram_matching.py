import cv2
import numpy as np
from skimage.exposure import match_histograms


def hist_match(source_img, template_img, multichannel):
    if multichannel:
        # Initialize output image
        matched_img = np.zeros_like(source_img)
        # Process each channel separately
        for channel in range(source_img.shape[2]):
            matched_img[:,:,channel] = hist_match(source_img[:,:,channel], template_img[:,:,channel], False)
        return matched_img
    else:
        # Compute the histograms and the cumulative histograms
        source_hist, _ = np.histogram(source_img.flatten(), 256, [0,256])
        template_hist, _ = np.histogram(template_img.flatten(), 256, [0,256])

        source_cumulative_hist = source_hist.cumsum()
        template_cumulative_hist = template_hist.cumsum()

        # Normalize the cumulative histograms
        source_cumulative_hist = (source_cumulative_hist - source_cumulative_hist.min()) * 255 / (source_cumulative_hist.max() - source_cumulative_hist.min())
        template_cumulative_hist = (template_cumulative_hist - template_cumulative_hist.min()) * 255 / (template_cumulative_hist.max() - template_cumulative_hist.min())

        # Use the cumulative histograms to map the values from the source image to the template image
        pixel_map = np.round(np.interp(source_cumulative_hist, template_cumulative_hist, np.arange(256))).astype('uint8')
        matched_img = pixel_map[source_img]

        return matched_img

# Load the source and template images
source_img = cv2.imread('blue-moon.jpg')
template_img = cv2.imread('purple-moon.jpg')

# Match the histograms
# matched_img = hist_match(source_img, template_img, True)
matched_img = match_histograms(source_img, template_img, multichannel=True)


# Save the result
cv2.imshow('matched', matched_img)
cv2.imshow('source', source_img)
cv2.imshow('template', template_img)
cv2.waitKey(0)
cv2.destroyAllWindows()