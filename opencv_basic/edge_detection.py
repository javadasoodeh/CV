import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.widgets import Slider

# Load and convert the image to grayscale
image = cv2.imread('HBD.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plt.subplots_adjust(bottom=0.25)

# Initialize T1 and T2 values
T1_initial = 0
T2_initial = np.max(gray_image)

# Apply Canny edge detection with initial T1 and T2 values
edges = cv2.Canny(gray_image, T1_initial, T2_initial)

# Display the original image in the first subplot
ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax1.set_title('Original Image')

# Display the edges in the second subplot
edges_plot = ax2.imshow(edges, cmap='gray')
ax2.set_title('Canny Edges')

# Create sliders for T1 and T2
ax_T1 = plt.axes([0.2, 0.1, 0.6, 0.03])
ax_T2 = plt.axes([0.2, 0.05, 0.6, 0.03])
slider_T1 = Slider(ax_T1, 'T1', 0, np.max(gray_image), valinit=T1_initial)
slider_T2 = Slider(ax_T2, 'T2', 0, np.max(gray_image), valinit=T2_initial)

# Define the update function for the sliders
def update(val):
    T1 = slider_T1.val
    T2 = slider_T2.val
    edges = cv2.Canny(gray_image, T1, T2)
    edges_plot.set_data(edges)
    fig.canvas.draw_idle()

# Bind the update function to the slider values
slider_T1.on_changed(update)
slider_T2.on_changed(update)

# Display the plot
plt.show()
