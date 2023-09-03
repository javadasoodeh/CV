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
| House features (size, location, number of rooms, etc.)	| Price	| Housing price prediction |


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

\# TODO add images

## What is a Classification Problem?

Classification is another type of supervised learning, 
but instead of predicting a continuous value, we are sorting data into categories. 
In our example, the categories are straightforward: either the presence or absence of breast cancer in a tissue sample.

In classification, the output variable (or label) is a category such as 'Yes' or 'No', 'True' or 'False', 
or 'Type A', 'Type B', and 'Type C'. In the case of breast cancer detection, we may have features like cell size, 
cell shape, and other metrics obtained from medical images. The model then learns to predict if the sample is
 malignant or benign based on these features.
 
### Breast Cancer Detection with One Input
Let's consider a simplified example where we are using just one feature—let's say, cell size—to classify 
the tissue as malignant or benign. We'll plot this on a graph where the x-axis represents cell size 
and the y-axis represents whether the tissue is malignant (1) or benign (0).

<p align="center">

<img src="/machine_learning_basic/Breast-Cancer-Detection-with-One-Input.jpg" alt="housing price - line" width="550">

</p> 

- The triangles represent malignant tissue samples, while the circles represent benign samples.
- The x-axis represents cell size, an important feature for our classification.
- The red dashed line is the "Decision Boundary." In this simple example, it lies at 0.5 on the y-axis. Any data point above this line would be classified as malignant, and any point below would be considered benign.

### Breast Cancer Detection with Multiple Input

<p align="center">

<img src="/machine_learning_basic/Breast-Cancer-Detection-with-Multiple-Input.jpg" alt="housing price - line" width="550">

</p> 

**Markers:** The red triangles represent malignant tissue samples, and the blue circles represent benign samples. Also, The black square represents the new patient. The coordinates correspond to the measured cell size and cell shape for this patient.

**Features:** The x-axis represents cell size, and the y-axis represents cell shape, both critical features for our classification task.

**Decision Boundary:** The color gradient represents the decision boundary generated by a model. The boundary separates the area into regions of predicted malignancy or benignity based on the features.

**Diagnosis for the New Patient**

According to our model, the predicted diagnosis for the new patient is 1, which indicates that the tissue is likely to be malignant.

The decision is based on the patient's position relative to the decision boundary in the feature space. As the point lies in the region classified as 'Malignant' by our model, the prediction is in line with that classification.

This illustrative example encapsulates how machine learning can assist healthcare professionals in making quicker and more accurate decisions. However, it's crucial to note that in a real-world clinical setting, multiple tests and expert evaluations are generally used in conjunction to arrive at a final diagnosis.

## Comparing Regression and Classification

By now, you might have noticed some fundamental differences between regression and classification:

**Type of Output:** In regression, the output is continuous, like the price of a house. In classification, the output is categorical, like identifying whether a tissue sample is malignant or benign.

**Decision Boundary:** In regression, there's no concept of a decision boundary. In classification, the decision boundary separates different classes.

**Objective:** In regression, we aim to minimize the difference between the predicted and actual continuous values. In classification, we aim to place data points in the correct categories.

**Examples:** Regression is often used for tasks like price prediction, weather forecasting, and stock market analysis. Classification is used in applications like spam filtering, disease diagnosis, and sentiment analysis.

 