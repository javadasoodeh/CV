## Introduction to Deep Learning

### What Is Deep Learning?
Deep Learning is a subfield of machine learning that focuses on training computers to learn from and make decisions based on data, 
similar to how humans learn from experience. Here's how to understand deep learning:

- **Inspiration from the Human Brain:** Imagine how our brains function with billions of neurons interconnected. Deep learning models mimic this structure using something called "artificial neural networks."

- **Pattern Recognition:** Just like a child learns to recognize a cat by observing various cats of different sizes, colors, and poses, deep learning models "learn" by processing vast amounts of data. Over time, they identify patterns in this data.

- **Layers of Learning:** The term "deep" in deep learning refers to the number of layers in these neural networks. With more layers, these models can recognize more complex patterns. Think of it like this: the first layer might recognize simple edges, the next layer identifies shapes by combining edges, the subsequent layers might recognize textures, and so on. By the time we get to the final layers, the model has a comprehensive understanding of the data, be it an image, a sound, or a text.

- **Automatic Feature Extraction:** Unlike traditional methods where humans have to specify what features a machine should recognize, deep learning models automatically figure out the features that are important.

\#Todo add images

### Single-layer Neural Networks (Perceptron)

A perceptron is the simplest form of a neural network used for binary classification. Here’s a more detailed breakdown:

- **Inputs:** These are the data or features that you provide to the network for processing. They can be anything from pixel values in an image to any other form of data.

- **Weights:** Associated with each input, a weight represents the importance of that particular input for the output. During the learning phase, the network adjusts these weights based on the error of the prediction.

- **Bias:** This is a constant value that provides the neuron with the flexibility to better fit the data. It's like an added tuning knob for the neuron's output.

- **Weighted Sum:** Before passing it to the activation function, the perceptron computes the weighted sum. It multiplies each input by its associated weight, sums up all these products, and then add the bias. Mathematically, if we have inputs $x_1, x_2,..., x_n$ and weights $w_1, w_2,..., w_n$, the weighted sum (often termed as net input), and the bias $b$ would be  $ \sum_{i=1}^{n} x_i w_i + b$.

- **Step Function (Activation Function):** The weighted sum is then passed through an activation function. For a basic perceptron, this is typically a step function, which produces a binary output. This function can take various forms, such as sigmoid, ReLU (Rectified Linear Unit), tanh (hyperbolic tangent), etc. If the weighted sum is above a certain threshold, the neuron fires (produces an output of 1), otherwise, it doesn't (produces an output of 0). By and large, The goal of the activation function is to introduce non-linearity into the neural network, allowing it to learn and represent complex relationships in the data.

- **Output:** The result of the step function determines the perceptron's output. For binary classification tasks, this would typically be a "0" or a "1".

<p align="center">

<img src="/deep_learning_basic/img/perceptron.jpg" alt="Perceptron" width="550"> 

</p>

### Multi-layer Neural Networks 

When we move beyond a single layer and start stacking multiple layers of these neurons, we have what's called a multi-layer neural network or more commonly, a multi-layer perceptron (MLP). This typically consists of:

* **Input Layer:** The layer that receives input from the dataset.
* **Hidden Layers:** Layers in between the input and output layers. The complexity of the neural network increases with more hidden layers, allowing it to capture intricate patterns and relationships in the data.
* **Output Layer:** The final layer that produces the result for given inputs.

### Difference between Deep Learning and Traditional Machine Learning

At a high level, traditional machine learning algorithms are often hand-crafted and require feature engineering, which means that the inputs must be transformed or tweaked to improve the model's performance. In contrast, deep learning models, especially Convolutional Neural Networks (CNNs) for images, are adept at automatically extracting features from raw data.

**Example Pipeline for Input Images:**

*Traditional Machine Learning:*
1. Pre-process the image (resize, normalize).
2. Manually extract features (edges, textures, color histograms).
3. Use these features as input to a machine learning model like SVM or Random Forest.
4. Model predicts the output based on the features.

*Deep Learning:*
1. Pre-process the image (resize, normalize).
2. Feed the image directly into a deep learning model (e.g., CNN).
3. The model automatically extracts hierarchical features and processes them through multiple layers.
4. Model predicts the output based on the learned features.

In essence, while traditional machine learning requires manual effort to extract meaningful features from images, deep learning automates this process, allowing for a more direct and often more accurate mapping between raw input data and the desired output.

