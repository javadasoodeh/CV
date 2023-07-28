# Section 2.1: An Introduction to Supervised Learning

In the context of machine learning, supervised learning is a type of learning paradigm where a model is trained using a labeled dataset, consisting of input data along with their corresponding desired output or target values. The goal of supervised learning is to enable the model to learn the mapping between inputs and outputs, so it can make accurate predictions on new, unseen data. It is called supervised learning because the process of an algorithm learning from the training dataset can be thought of as a teacher supervising the learning process. We know the correct answers, and the algorithm iteratively makes predictions on the training data and is corrected by the teacher. Learning stops when the algorithm achieves an acceptable level of performance.

Here are some examples of supervised learning applications:

| Input (X)           | Output (Y)           | Application   |
| :---              |    :----:            |          ---: |
| Email content	| Spam or not spam	|Spam filtering |
| Customer demographic data, purchase history	| Will make a purchase in the next month or not	| Customer retention prediction |
| Patient health records	| Presence or absence of disease	| Medical diagnosis|
| House features (size, location, number of rooms, etc.)	| Price	| Real estate price prediction |


## Visualizing Supervised Learning with Regression

To visually understand how supervised learning works, let's consider a simple regression problem. Regression is a type of supervised learning where the output (Y) is a continuous value (as opposed to classification where Y is a discrete label).
A common example of a regression problem is predicting house prices based on various features. For simplicity, let's consider only one feature: the size of the house. The size of the house (X) is the input, and the price of the house (Y) is the output.
We can visualize this as a 2-dimensional plot where the x-axis represents the size of the house and the y-axis represents the price of the house. Each point in this plot represents a house. The goal of the learning algorithm is to fit a line (or in more complex scenarios, a curve) that best captures the relationship between the size and the price.
Let's generate some sample data and fit a line to it. Note that in a real-world application, we would use a machine learning library to fit a line using a method like least squares, but for this illustration, we'll manually fit a line to keep things simple.

Let's take, for example, a house of size 5 (the x-axis value). The corresponding price according to our model (the red line) would be approximately 2×5=102×5=10 (the y-axis value).

<p align="center">

<img src="/machine_learning_basic/housing-price.jpg" alt="housing price - line" width="550">

</p> 

Let’s add another model (the blue line):

<p align="center">
<img src="/machine_learning_basic/housing-price2.jpg" alt="housing price - curve" width="550">
</p> 

As you can see, the predicted price for the same house can vary significantly depending on the model used (linear or curved). 

- The green point and dashed line represent the predicted price for a house of size 5 according to our initial linear model (red line).
- The purple point and dashed line represent the predicted price for the same house according to the new curve (blue line).

