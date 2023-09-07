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

- _(**Training Data** feeds into --> **Learning Algorithm** which produces --> **Function $f$**)_ 

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





