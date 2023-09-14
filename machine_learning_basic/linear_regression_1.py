import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Given data
square_footage = np.array([650, 785, 1200, 1400, 1540, 1650, 1725, 1850, 2100, 2300])
housing_price = np.array([772000, 998000, 1208500, 1412000, 1534500, 1650250, 1725000, 1857500, 2120000, 2305000])


# Predict function
def predict_price(x, w, b):
    # Preallocate an array of zeros with the same shape as x
    predicted_prices = np.zeros_like(x)

    # Loop through each index and value in x
    for i, value in enumerate(x):
        # Compute the predicted price for the current value of x using the linear equation
        predicted_prices[i] = w * value + b

    return predicted_prices


# Setting up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Initial values for w and b
initial_w = 1000
initial_b = 50000

# Plotting the initial data and model
plt.scatter(square_footage, housing_price, color='blue', label='Training Data')
line, = plt.plot(square_footage, predict_price(square_footage, initial_w, initial_b), 'r-', label='Linear Model')
plt.xlabel('Square Footage')
plt.ylabel('Housing Price')
plt.title('Housing Price Prediction')
plt.grid(True)

# Display the initial function as text above the sliders
function_text = plt.text(0.15, 0.02, f'f(x) = {initial_w}x + {initial_b}', color='red', transform=plt.gcf().transFigure)

# Adding sliders for w and b
ax_slider_w = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_b = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_w = Slider(ax_slider_w, 'w (Slope)', 500, 1500, valinit=initial_w, valstep=10)
slider_b = Slider(ax_slider_b, 'b (Intercept)', -100000, 200000, valinit=initial_b, valstep=500)


# Update function to redraw the model when w or b changes
def update(val):
    w = slider_w.val
    b = slider_b.val
    line.set_ydata(predict_price(square_footage, w, b))
    function_text.set_text(f'f(x) = {w:.2f}x + {b:.2f}')
    fig.canvas.draw_idle()


# Attach the update function toa changes in the slider values
slider_w.on_changed(update)
slider_b.on_changed(update)

plt.legend()
plt.show()
