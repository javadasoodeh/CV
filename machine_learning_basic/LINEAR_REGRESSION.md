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

In machine learning, when we refer to a **training set**, we're talking about the dataset we use to train our model. 
This set includes both the input data (in our case, square footage) and the correct answers (in our case, housing prices). 
The model uses this data to learn the relationships between inputs and outputs.

**Standard Notation**:
- $m$: Number of training examples.
- $x$: "Input" variable/features (Square Footage in our example).
- $y$: "Output" or "target" variable/label (Housing Price in our example).
- $(x^{(i)}, y^{(i)})$: Represents the $i^{th}$ training example.

For our dataset:
- $m = 10$ (since we have 10 houses in our dataset).
- $x^{(1)} = 650$ and $y^{(1)} = $772,000$ represent the square footage and housing price of the first house, respectively.
- $x^{(2)} = 785$ and $y^{(2)} = $998,000$ represent the square footage and housing price of the second house, and so on.

Using this notation provides a standardized way to reference the elements of our training set, 
making it easier to describe algorithms and mathematical operations on the data.

### Supervised Learning Algorithms

When we delve into the world of supervised learning, we're essentially exploring algorithms that learn from labeled training data to make predictions. This learning process revolves around determining a function that links inputs to desired outputs. Let's break down this process step by step.

### The Supervised Learning Process

Conceptually, the supervised learning process can be distilled into three primary stages:

1. **Training Data**: Our starting point consists of a training dataset. Each piece of data in this set pairs an input with its correct output.
2. **Learning Algorithm**: This dataset is then channeled into a learning algorithm tailored to analyze and process the data.
3. **Output Function**: Post processing, the algorithm yields a function (commonly denoted as $f$).

### Visual Representation:

- _**Training Data** feeds into --> **Learning Algorithm** which produces --> **Function $f$**_ 

Using the housing price prediction as an illustrative example:

- **Training Data**: We possess data of houses along with their square footages and their respective prices.
- **Learning Algorithm**: For our example, we'll employ a linear regression model.
- **Output Function**: The culmination of this process sees the model outputting a function $f$. When introduced to the square footage of a new house, this function endeavors to predict its price.

When we input a new house's square footage (let's consider 1250 sq. ft. for this instance) into our function $f$, it endeavors to estimate the price based on its prior learning from the training data.

## Mathematical Foundations of the Process

For our current housing narrative, we're postulating that $f$ is a linear entity, symbolizing a straight-line relationship. Consequently, the function can be mathematically represented as:

$$ f(x) = w x + b$$

Where:

- $f(x)$ symbolizes the projected housing price.
- $x$ stands for the square footage of the house.
- $b$ represents the y-intercept of the line.
- $w$ is the slope of the line.

The learning algorithm's principal task is pinpointing the optimal values for $b$ and $w$. These values should ideally render $f(x)$ as a credible predictor of the housing price for any given square footage $x$.

<p align="center">

<img src="/machine_learning_basic/Housing-Price-Prediction-Linear.jpg" alt="housing price prediction linear" width="550">

</p> 

In the visualization:

- **Blue Points**: Represent our foundational training data. Each distinct point corresponds to a house, with its positioning determined by the square footage and the actual price.
  
- **Red Line**: Symbolizes the function $f$ that our linear regression algorithm crafted. For any given square footage $x$, the function $f$ endeavors to estimate the housing price.

This function $f$ is linear because we're leveraging a linear regression model with a singular variable (square footage). The mathematical embodiment of this line, as illustrated earlier, is $f(x) = w x + b$. Here, $b$ signifies the point where the line intersects the y-axis (y-intercept), while $w$ establishes the slope of the line.

We're opting for a linear function in this instance as a foundational step. It's intuitive, straightforward, and can act as a precursor to more intricate, non-linear functions. The model we've engaged with, where we're predicting a continuous outcome based on one variable via a straight line, is termed **linear regression with one variable**. 

As we evolve our understanding, we can include multiple variables or even leverage non-linear functions to encapsulate more nuanced patterns in the data. Nevertheless, grasping this foundational model is pivotal before diving into those advanced layers.





