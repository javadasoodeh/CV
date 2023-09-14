# Supervised Learning and Linear Regression
In this section, we are going to explore the overall process of supervised learning and delve deeper into 
one specific learning algorithm: linear regression. To build your intuition about it, let's revisit 
the housing price prediction example we discussed earlier.

At its core, linear regression is a foundational machine learning technique that aims to predict a value 
based on the input provided. Think of it like drawing a straight line through a set of data points in a way 
that best captures the underlying trend.
  
  let's start with the graph illustrating the housing price prediction based on square footage. 
  
<p align="center">

<img src="/machine_learning_basic/Housing-Price-Prediction.jpg" alt="housing price prediction" width="550">

</p> 
  
  
  Each point on the graph represents a house, with its position determined by its square footage and its corresponding price.
  
  Below is the data table representing the same:
  
  | Square Footage | Housing Price |
|----------------|---------------|
| 650            | $772,000      |
| 785            | $998,000      |
| 1,200          | $1,208,500    |
| 1,400          | $1,412,000    |
| 1,540          | $1,534,500    |
| 1,650          | $1,650,250    |
| 1,725          | $1,725,000    |
| 1,850          | $1,857,500    |
| 2,100          | $2,120,000    |
| 2,300          | $2,305,000    |

## Training Set and Its Notation

In machine learning, when we refer to a **training set/data**, we're talking about the dataset we use to train our model. 
This set includes both the input data (in our case, square footage) and the correct answers (in our case, housing prices). 
The model uses this data to learn the relationships between inputs and outputs.

**Standard Notation**:
- $m$: Number of training examples.
- $x$: "Input" variable/features (Square Footage in our example).
- $y$: "Output" or "target" variable/label (Housing Price in our example).
- $(x^{(i)}, y^{(i)})$: Represents the $i^{th}$ training example.

For our dataset:
- $m = 10$ (since we have 10 houses in our dataset).
- $x^{(1)} = 650$ and $y^{(1)}$ $=$ \$ $772,000$ represent the square footage and housing price of the first house, respectively.
- $x^{(2)} = 785$ and $y^{(2)}$ $=$ \$ $998,000$ represent the square footage and housing price of the second house, and so on.

Using this notation provides a standardized way to reference the elements of our training set, 
making it easier to describe algorithms and mathematical operations on the data.

### Supervised Learning Algorithms

When we talk about supervised learning, the fundamental idea is that we have an algorithm that learns from labeled training data, and makes predictions based on that data. This learning process involves finding a function that maps inputs to desired outputs. Let's understand this process step by step.

### How Supervised Learning Algorithms Work

At the highest level, the process can be visualized as follows:

1. **Training Data:** We begin with a set of training data. Each piece of data consists of an input paired with the correct output.
2. **Learning Algorithm:** This data is fed into a learning algorithm which processes the data.
3. **Output Function:** The algorithm then outputs a function (often denoted as **$f$**).

#### Diagram

- **Training Data** feeds into --> **Learning Algorithm** which produces --> **Function $f$** 

For our housing price prediction example:

- **Training Data**: We have data of houses with known square footages and their corresponding prices.
- **Learning Algorithm**: Let's say we use a linear regression model.
- **Output Function**: The model will produce a function **$f$** which, when given a new house's square footage, will predict its price.

Now, when we feed a new sample (say, a house with a square footage of 1250) into our function **$f$**, it provides an estimated price based on its learning from the training data.

## Mathematical Representation

For our housing scenario, since we're assuming **$f$** to be a straight line (linear relationship), the function can be represented as:

**$$ f(x) = w x + b$$**

Where:

- $f(x)$ is the estimated housing price.
- $x$ is the square footage of the house.
- $b$ is the y-intercept of the line.
- $w$ is the slope of the line.

In essence, the learning algorithm's job is to find the values of $b$ and $w$ that make $f(x)$ a good predictor of the housing price for any given square footage $x$.

Let's visualize this on a graph.

<p align="center">

<img src="/machine_learning_basic/Housing-Price-Prediction-Linear.jpeg" alt="housing price prediction linear" width="650">

</p> 

In the visualization:

- **Blue Points**: These represent our training data. Each point corresponds to a house, with its position determined by its square footage and its actual price.
  
- **Red Line**: This is the function **$f$** that our linear regression model produced. Given any square footage **$x$**, the function **$f$** will estimate the housing price.

This function $f$ is a straight line because we're using a linear regression model with one variable (square footage). The mathematical representation of this line is $f(x) = w x + b$. Here, $b$ is where the line intersects the y-axis (y-intercept), and $w$ determines the slope of the line.

We use a linear function in this scenario as a foundation. It's simple, interpretable, and can serve as a building block to more complex, non-linear functions. The model we've discussed, where we're predicting a continuous output based on one variable using a straight line, is referred to as **linear regression with one variable**.

In more advanced scenarios, we might incorporate multiple variables or use non-linear functions to capture more intricate patterns in the data. But understanding this foundational concept is crucial before diving into those complexities.


## Interactive Visualization of a Linear Regression Model using Python Code
Using the Python programming language, along with some powerful libraries, 
we'll show you an interactive demonstration of the linear regression model. 
This demonstration will allow you to adjust the parameters of the model and observe its behavior in real-time. 
Also, allow users to experiment and understand the role of `w` and `b` in the linear regression model.

### 1. Importing necessary libraries:

```python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

``` 

**1.1. `numpy`:**
- **Library Overview**: `numpy` (Numerical Python) is a core library for numerical computing in Python. It provides support for arrays (including matrices) and an assortment of mathematical functions to operate on these arrays. With `numpy`, scientific and mathematical computations are simpler and faster.
- **Usage in Code**: We use `numpy` to create and manipulate data arrays.

**1.2. `matplotlib.pyplot`:**
- **Library Overview**: `matplotlib` is a comprehensive library for creating static, animated, and interactive visualizations in Python. The `pyplot` module in `matplotlib` provides a MATLAB-like interface, making it easier to plot graphs and charts.
- **Usage in Code**: We use `matplotlib.pyplot` to visualize our dataset and the linear regression model on a graph.

**1.3. `Slider` from `matplotlib.widgets`:**
- **Library Overview**: The `matplotlib.widgets` module provides a set of classes for adding interactive elements (like sliders, buttons) to the plots.
- **Usage in Code**: We use the `Slider` class to create interactive sliders on the plot, allowing users to adjust the slope and y-intercept of the linear model in real-time.

### 2. Dataset:
```python

# Given data
square_footage = np.array([650, 785, 1200, 1400, 1540, 1650, 1725, 1850, 2100, 2300])
housing_price = np.array([772000, 998000, 1208500, 1412000, 1534500, 1650250, 1725000, 1857500, 2120000, 2305000])

```

**2.1. `np.array`:**
- **Function Overview**: `np.array` is a core function of `numpy`. It creates an array from any object exposing the array interface, or from any method that returns an array.
- **Parameters**:
  - The first argument is the object to be converted to an array.
  - It has several other optional parameters, but we're using the default settings in this code.
- **Usage in Code**: We're using `np.array` to create two arrays: `square_footage` (containing the area of the houses in square feet) and `housing_price` (containing the corresponding prices of these houses).

### 3. **Prediction Function**:

```python

# Predict function
def predict_price(x, w, b):
    # Preallocate an array of zeros with the same shape as x
    predicted_prices = np.zeros_like(x)

    # Loop through each index and value in x
    for i, value in enumerate(x):
        # Compute the predicted price for the current value of x using the linear equation
        predicted_prices[i] = w * value + b

    return predicted_prices
    
```


**3.1. `np.zeros_like`:**
- **Function Overview**: This `numpy` function returns an array of zeros with the same shape and type as the given array.
- **Parameters**: 
  - The array you want to replicate (in terms of shape and type).
- **Usage in Code**: We use `np.zeros_like(x)` to initialize the `predicted_prices` array with zeros. This array will eventually hold the predicted prices computed by our linear model.

**3.2. Loop & Linear Equation**:
- **Overview**: The loop iterates over each value in the `x` array (square footage values). For each value, it computes the predicted price using the linear equation \(f(x) = wx + b\).
- **Usage in Code**: This loop fills in the `predicted_prices` array with values computed by our linear model.

### 4. Setting up the Visualization:
The subsequent lines of code prepare the interactive plot.
```python

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

```

**4.1. `plt.subplots`:**
- **Function Overview**: Provides a way to plot multiple plots in a single figure. Often used due to its flexibility, even for single plots.
- **Parameters**:
  - `figsize`: A tuple defining the size of the figure in inches.
- **Usage**: Sets up a figure and axis for plotting with a specified size.

**4.2. `plt.subplots_adjust`:**
- **Function Overview**: This function from `matplotlib.pyplot` adjusts the subplot parameters to give specified padding. It's often used to ensure that subplots don't overlap or to make room for additional elements like sliders or legends.
- **Parameters**:
  - `bottom`: The bottom of the subplots for the figure. It represents the amount of space at the bottom of the figure (as a fraction of the figure height) to allow for things like labels, titles, or other interactive elements.
- **Usage in Code**: `plt.subplots_adjust(bottom=0.25)` ensures there's sufficient space at the bottom of the plot to accommodate the sliders.

**4.3. Initial values for `w` and `b`:**
- **Overview**: Before visualizing the linear regression model, we need to specify initial values for the slope (`w`) and y-intercept (`b`). These initial values give a starting point for the visualization.
- **Usage in Code**: We set `initial_w` to 1000 and `initial_b` to 50000. These values determine the initial appearance of the red line (linear model) on the graph.

**4.4. Plotting Data and Initial Model**:
**4.4.1. `plt.scatter`:**
- **Function Overview**: This function from `matplotlib.pyplot` creates a scatter plot. Each point corresponds to a pair of values, one from each of the input arrays.
- **Parameters**:
  - The first two arguments are arrays representing the x and y coordinates of the points.
  - `color`: Specifies the color of the points.
  - `label`: Provides a label for the data, which can later be used in a legend.
- **Usage in Code**: `plt.scatter(square_footage, housing_price, color='blue', label='Training Data')` plots the actual housing prices against the square footage as blue dots.

**4.4.2. `plt.plot`:**
- **Function Overview**: This function plots lines and/or markers to the axes. It's commonly used for plotting functions, like our linear model.
- **Parameters**:
  - The first two arguments are arrays representing the x and y coordinates of the line or marker. 
  - The third argument (`'r-'` in this case) is a format string that indicates the color and line type of the plot. `'r-'` stands for a red solid line.
  - `label`: Provides a label for the line, useful for legends.
- **Usage in Code**: The line `line, = plt.plot(...)` plots the initial linear model as a red line. The `predict_price` function calculates the y-values based on the initial `w` and `b`. The comma after `line,` is used to unpack the result returned by `plt.plot` into a single Line2D object.

**4.4.3. Other Plot Customizations**:
- **`plt.xlabel` and `plt.ylabel`**: These functions set the labels for the x and y axes respectively.
- **`plt.title`**: Sets the title of the plot.
- **`plt.grid`**: This function, when set to `True`, adds a grid to the plot which can help in reading the values more accurately.

**4.5. Displaying the Function f(x)**:

**4.5.1. `plt.text`**:
- **Function Overview**: This function in `matplotlib.pyplot` adds text to an arbitrary location on the axes. It can be used to provide additional information or annotations on the plot.
- **Parameters**:
  - The first two parameters (`0.15, 0.02`) specify the x and y coordinates of the text. These coordinates are given in a normalized figure coordinate system, where (0,0) is the bottom-left corner and (1,1) is the top-right.
  - The third parameter is the text string to be displayed. In this case, it displays the equation of the linear model based on the initial values of $w$ and $b$.
  - `color`: Specifies the color of the text.
  - `transform`: Determines the coordinate system to use. The `plt.gcf().transFigure` ensures the coordinates are in terms of the figure's width and height.
- **Usage in Code**: It displays the equation of the linear model above the sliders, providing a real-time view of the equation as sliders are adjusted.


### 5. **Interactive Sliders**:

```python

# Adding sliders for w and b
ax_slider_w = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_b = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_w = Slider(ax_slider_w, 'W (Slope)', 500, 1500, valinit=initial_w, valstep=10)
slider_b = Slider(ax_slider_b, 'B (Intercept)', -100000, 200000, valinit=initial_b, valstep=500)

```

**5.1. `plt.axes`**:
- **Function Overview**: This function in `matplotlib.pyplot` defines a region in the figure where an element, like a plot or a widget, will be placed.
- **Parameters**:
  - The list specifies the position and size of the region `[left, bottom, width, height]`, where all values are in fractional coordinates, with (0,0) being the bottom-left and (1,1) the top-right of the figure.
  - `facecolor`: Specifies the background color of the region.
- **Usage in Code**: Two regions are defined (`ax_slider_w` and `ax_slider_b`) to place the sliders for adjusting the slope $w$ and y-intercept $b$ respectively.

**5.2. `Slider`**:
- **Function Overview**: This class from `matplotlib.widgets` creates an interactive slider on the defined axes.
- **Parameters**:
  - `ax`: Specifies the region where the slider will be placed.
  - `label`: A label for the slider.
  - `valmin` and `valmax`: Define the minimum and maximum values for the slider.
  - `valinit`: The initial value of the slider.
  - `valstep`: The increment by which the slider value changes.
- **Usage in Code**: Two sliders are created (`slider_w` for the slope $w$ and `slider_b` for the y-intercept $b$). Users can adjust these sliders to interactively modify the linear model.


### 6. **Update Function and Interactivity**:

```python

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

```
**6.1. `update` function**:
- **Overview**: This function is triggered every time the value of a slider changes. It recalculates the predicted housing prices using the new values of $w$ and $b$ from the sliders. The function then updates the plot to reflect these changes.
- **Key Lines**:
  - `line.set_ydata(predict_price(square_footage, w, b))`: Updates the y-values of the linear model on the plot.
  - `function_text.set_text(f'f(x) = {w:.2f}x + {b:.2f}')`: Updates the displayed equation of the linear model.
  - `fig.canvas.draw_idle()`: Redraws the figure with the updated data.

**6.2. `on_changed` event**:
- **Overview**: This method from the `Slider` class attaches a function to the slider. When the slider value changes, the attached function gets triggered.
- **Usage in Code**: The `update` function is attached to both sliders. So, whenever a user adjusts either of the sliders, the `update` function is executed, and the plot updates accordingly.

### 7. **Displaying the Visualization**:

```python

plt.legend()
plt.show()

```

**7.1. `plt.legend`**:
- **Function Overview**: This function in `matplotlib.pyplot` displays a legend on the plot. The legend provides labels for different elements on the plot, making it easier to interpret.
- **Usage in Code**: It displays the labels 'Training Data' for the scatter plot points and 'Linear Model' for the red line.

**7.2. `plt.show`**:
- **Function Overview**: This function in `matplotlib.pyplot` displays the figure. It's the culmination of all the plotting commands and displays the final visualization.
- **Usage in Code**: It renders the entire plot, complete with the data points, linear model, sliders, and labels.

### output 

After you run <a href="linear_regression_1.py" >the code</a>, you are able to to adjust the parameters ($w$, $b$) of the model and observe its behavior in real-time.

<p align="center">
<img src="/machine_learning_basic/Linear-Regression-1.jpg" alt="housing price - line" width="550">
</p> 


### Cost Function: An Overview

When training a model, we aim to find the best possible parameters (in our case, $w$ and $b$) such that the predictions made by the model are as close as possible to the actual values. But how do we quantify "as close as possible"? This is where the cost function comes into play.

The cost function, often denoted as $J$, quantifies the difference between the predicted values and the actual values. In essence, it measures the "cost" or "error" of using a particular set of parameters.

### The Goal

The primary objective of a learning algorithm is to minimize the cost function. In mathematical terms, our goal is:

$\text{Minimize } J(w, b)$

### Visualizing on the Linear Regression Graph

When we plot our training data and the linear regression line, the difference between the actual price (target $y$) and the predicted price (estimated $\hat{y}$) for each data point is the vertical distance between the point and the line.

The goal of the cost function is to find values for $w$ and $b$ such that the sum of these vertical distances (squared) across all data points is minimized. Essentially, we want our line (described by $w$ and $b$) to be as close as possible to all data points.

### Cost Function for Linear Regression

For our linear regression model, a commonly used cost function is the Mean Squared Error (MSE). It is defined as:

$$J(w, b) = \frac{1}{2m} \sum_{i=1}^m (\hat{y}^{(i)} - y^{(i)})^2$$

Where:
- $m$ is the number of training examples.
- $\hat{y}^{(i)}$ is the predicted value for the $i^{th}$ training example.
- $y^{(i)}$ is the actual value for the $i^{th}$ training example.

Breaking it down:
1. $\hat{y}^{(i)} - y^{(i)}$: This represents the difference between the predicted and actual values for the $i^{th}$ training example.
2. Why square the difference? Squaring ensures that all differences are positive and emphasizes larger differences. For instance, an error of 10 is not just twice as bad as an error of 5; it's four times worse.
3. $\frac{1}{2m}$: Averaging the squared differences gives us the mean squared error. The factor of $\frac{1}{2}$ is often included for mathematical convenience when deriving gradient descent equations (it cancels out the square's power when differentiated).

In essence, the cost function tells us how "off" our predictions are when using a specific $w$ and $b$. By minimizing this function, we adjust $w$ and $b$ to get the best possible linear regression line for our data.

Now, let's visualize the training data, the linear regression line, and the differences (errors) between the predictions and actual values on a graph.

<p align="center">
<img src="/machine_learning_basic/Cost-Function-1.jpg" alt="housing price - cost function" width="550">
</p> 


