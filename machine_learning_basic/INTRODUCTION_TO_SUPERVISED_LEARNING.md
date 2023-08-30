# Section 2.1: An Introduction to Supervised Learning

In supervised learning, we train a model on a labeled dataset, which means each training example is paired with an output label. 
The goal of supervised learning is to enable the model to learn the mapping between inputs and outputs, 
so it can make accurate predictions on new, unseen data. It is called supervised learning because 
the process of an algorithm learning from the training dataset can be thought of as a teacher 
supervising the learning process. We know the correct answers, and the algorithm iteratively 
makes predictions on the training data and is corrected by the teacher. Learning stops when 
the algorithm achieves an acceptable level of performance.

Here are some examples of supervised learning applications:

| Input (X)           | Output (Y)           | Application   |
| :---              |    :----:            |          ---: |
| Email content	| Spam or not spam	|Spam filtering |
| Customer demographic data, purchase history	| Will make a purchase in the next month or not	| Customer retention prediction |
| Patient health records	| Presence or absence of disease	| Medical diagnosis|
| House features (size, location, number of rooms, etc.)	| Price	| Real estate price prediction |


## Housing Price Prediction

Let's delve into the example of housing price prediction. 
Imagine you have data on house prices in a certain city, along with features like the number of bedrooms, 
square footage, and the year it was built. Your goal is to predict the selling price of new houses based on these features.

To visualize this, let's say we're focusing on just one feature—square footage—and we want to predict 
the price based on that. We can plot the data on a graph where the x-axis represents square footage and
 the y-axis represents the price. We'll also plot two different models and see how they predict prices 
 for a specific square footage.

<p align="center">

<img src="/machine_learning_basic/housing-price.jpg" alt="housing price - line" width="550">

</p> 

Graph description:

- The blue dots represent the actual prices of houses based on their square footage.
- The green line is a model that predicts housing prices using a linear equation. This is what we often call a "Linear Model."
- The red line represents another model that predicts housing prices using a quadratic equation, which we'll refer to as the "Quadratic Model."
- The gray dashed lines indicate a specific square footage we're interested in exploring (1,500 sqft in this case).
- The gray and purple dashed lines on the y-axis show the predicted prices for the house with 1,500 sqft according to the Linear and Quadratic Models, respectively.

As you can see, the predicted price for the same house can vary significantly depending on the model used (linear or quadratic).

- The green arrow points to the price predicted by the Linear Model for a house with 1,500 sqft. The prediction is around $275,000.
- The red arrow indicates the price predicted by the Quadratic Model for the same house, which is approximately $267,500.

### Regression

At this point, you may have observed that we employed two distinct models—the Linear Model 
and the Quadratic Model—to forecast the house price based on its square footage. 
This exercise of **predicting a continuous output** (house price, in this case) 
from one or more input features (square footage here) is known as **regression** in machine learning.

The goal of the learning algorithm in regression is to fit a line (or in more complex scenarios, a curve)
 that best captures the relationship between the input features and the output label. 
 In our housing price prediction example, the algorithm tries to find the line or curve that 
 most accurately represents the relationship between the square footage of the house and its price.


\# TODO add classification 
\# TODO add images 