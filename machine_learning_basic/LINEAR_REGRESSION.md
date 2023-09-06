# Supervised Learning and Linear Regression
In this section, we are going to explore the overall process of supervised learning and delve deeper into 
one specific learning algorithm: linear regression. To build your intuition about it, let's revisit 
the housing price prediction example we discussed earlier.

At its core, linear regression is a foundational machine learning technique that aims to predict a value 
based on the input provided. Think of it like drawing a straight line through a set of data points in a way 
that best captures the underlying trend.
  
  Here's the graph illustrating the housing price prediction based on square footage. 
  
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




