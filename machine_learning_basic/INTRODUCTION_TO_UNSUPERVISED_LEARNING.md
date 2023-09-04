# Introduction to Unsupervised Learning
Machine learning isn't always about making predictions with labels in hand. Sometimes, we have data without any labels, and we need to find hidden structures within it. This is where unsupervised learning comes into play.

# What is Unsupervised Learning?
Unsupervised learning is a type of machine learning where algorithms learn from data without explicit labels, aiming to identify patterns, groupings, or structures. Unlike supervised learning, where we train algorithms using labeled data, in unsupervised learning, we only have input data (features) and no corresponding output variables.

# Why do we say "Unsupervised"?
The term "unsupervised" refers to the fact that these algorithms are not guided or supervised by any prior knowledge about the outcome. Instead, they discover the inherent structures in the data on their own.

# Breast Cancer Detection: A New Perspective
Let’s take our previous breast cancer detection example to build intuition. In our supervised learning scenario, 
we used labeled data (cell size, cell shape) to predict whether a tissue sample was malignant or benign.

But let's imagine a scenario where a lab technician has just started collecting cell size and shape data, 
but hasn’t yet labeled any of them as benign or malignant. This is where unsupervised learning, 
specifically clustering, can come in handy.

- **_Clustering in the Context of Breast Cancer Detection_**
**Clustering** is a method of grouping data points in such a way that data points in the same group (or cluster) are
 more similar to each other than to those in other groups. let's visualize the scenario for the breast cancer example; 
 we aim to group tissue samples based on their features (cell size and shape). 
 Our hope would be that these natural groupings might correspond to benign and malignant samples.

    <p align="center">
    
    <img src="/machine_learning_basic/Clustering-Breast-Cancer-Detection.jpg" alt="Clustring Breaset Cancer Detection" width="550">
    
    </p> 

   **Data Points:** Each point represents a tissue sample, with its position determined by the cell size and cell shape.

   **Clusters:** We've used a clustering algorithm to group these samples into two clusters. These clusters are visually represented by the two circles in the graph, with the 'x' marking the centroid (or the center) of each cluster.

   **Labels:** In unsupervised learning, we don't have prior knowledge about what each cluster represents (i.e., benign or malignant). Instead, the algorithm tries to find natural groupings in the data. It's up to us (or medical experts) to interpret the meaning of these clusters based on further investigation or domain knowledge.

However, there's a critical distinction:

**Supervised Learning:** We tell the algorithm which samples are benign and which are malignant, and it learns the pattern.

**Unsupervised Learning (Clustering):** The algorithm tries to find groupings on its own. Our job is to then interpret these clusters. For instance, one cluster might largely represent benign samples, while another might represent malignant ones.

# Applications of Clustering
Clustering has a wide array of applications across various domains:

**Market Segmentation:** Businesses use clustering to segment their customers into different groups based on purchasing behavior, demographics, etc. This helps tailor marketing strategies for each group. In clustering terms, each customer's purchasing history might be a feature, and the goal is to find groups of customers with similar purchasing behaviors.

**Document Classification:** Clustering can be used to group articles or documents of similar topics. Here, the features might be the frequency of words or phrases, and the clusters represent articles that talk about similar topics.

**Image Segmentation:** In image processing, clustering can segment different regions or objects in an image. The features can be pixel values, textures, colors, etc., and clusters might represent different objects or regions in the image.

**Recommendation Systems:** Websites like Amazon or Netflix use clustering to recommend products or movies. They group items based on features like genre, director, actor, etc., and if a user likes one item in a cluster, they might like others in the same cluster.

**Anomaly Detection:** Clustering can also be used to detect anomalies. In a dataset, anomalies are typically far from any cluster. For instance, in credit card transaction data, clusters might represent typical purchasing patterns, while anomalies might indicate fraud.

In each of these applications, the mechanism of clustering remains similar: **group data points based on their features**. However, the nature of the features and the interpretation of the clusters vary based on the domain and the specific problem.