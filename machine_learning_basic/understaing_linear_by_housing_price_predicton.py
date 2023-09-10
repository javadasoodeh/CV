import numpy as np
import matplotlib.pyplot as plt

# Given data
square_footage = np.array([650, 785, 1200, 1400, 1540, 1650, 1725, 1850, 2100, 2300])
housing_price = np.array([772000, 998000, 1208500, 1412000, 1534500, 1650250, 1725000, 1857500, 2120000, 2305000])


# Predict function
def predict_price(x, w, b):
    return w * x + b


# Visualization function
def plot_data_and_model(w, b):
    plt.scatter(square_footage, housing_price, color='blue', label='Training Data')

    # Predict prices based on the user-defined w and b
    predicted_prices = predict_price(square_footage, w, b)

    plt.plot(square_footage, predicted_prices, color='red', label=f'Linear Model: y = {w}x + {b}')
    plt.xlabel('Square Footage')
    plt.ylabel('Housing Price')
    plt.title('Housing Price Prediction')
    plt.legend()
    plt.grid(True)
    plt.show()


# Plotting with example values for w and b
plot_data_and_model(1000, 50000)
