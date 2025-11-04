# 100DaysOfML

## Day 4:
Batch Learning: The model is trained on the entire dataset at once.
Online Learning: The model is trained incrementally as new data arrives.

Disadvantages of Batch Learning:
1. High Memory Usage
2. Slow Adaptation to New Data
3. Computationally Intensive
4. Not Suitable for Real-Time Applications
5. Requires Complete Dataset
6. Difficult to Scale

## Day 9:
Day 5 of Campus X 100 Days of Machine Learning

Online Learning:
1. Incremental Updates
2. Lower Memory Usage
3. Real-Time Adaptation
4. Suitable for Streaming Data
5. Scalability
6. Continuous Learning

### When to Use Batch Learning vs Online Learning:
- Use Batch Learning when you have a static dataset and sufficient computational resources.
- Use Online Learning when dealing with streaming data or when the dataset is too large to fit into memory.
- Consider the need for real-time predictions and adaptability to new data when choosing between the two approaches.
- Evaluate the trade-offs between accuracy and computational efficiency based on the specific application requirements.
- Batch Learning is ideal for scenarios where model accuracy is paramount and the dataset is stable.
- Online Learning is preferable in dynamic environments where data evolves over time and quick adaptation is necessary.
- Hybrid approaches can also be considered, where a model is initially trained using batch learning and then updated using online learning techniques as new data becomes available.
- Always assess the specific use case, data characteristics, and resource constraints before deciding on the learning approach.

### When to Use Online Learning:
1. Where there is a concept drift
2. Cost effective
3. Faster solution

### How to Implement Online Learning:
1. Choose an appropriate online learning algorithm (e.g., Stochastic Gradient Descent, Perceptron).
2. Initialize the model parameters.
3. For each incoming data point or mini-batch:
   a. Make a prediction using the current model.
   b. Calculate the error based on the prediction and the actual label.
   c. Update the model parameters using the error and a predefined learning rate.
4. Repeat the process as new data arrives.
5. Periodically evaluate the model's performance on a validation set to ensure it is learning effectively.
6. Adjust hyperparameters (e.g., learning rate) as necessary to optimize performance.   
7. Implement mechanisms to handle concept drift, such as forgetting older data or using adaptive learning rates.
8. Monitor resource usage to ensure the online learning process remains efficient.
9. Consider using mini-batches instead of single data points to balance between convergence speed and stability.
10. Document the online learning process and any changes made to the model for future reference.

### Libraries for Online Learning:
1. Scikit-learn: Provides implementations of various online learning algorithms like SGDClassifier and Perceptron.
2. River: A dedicated library for online machine learning that offers a wide range of algorithms and tools for streaming data.
3. Vowpal Wabbit: An efficient online learning system that supports large-scale machine learning tasks.
4. TensorFlow: While primarily used for deep learning, TensorFlow can be adapted for online learning through custom training loops.
5. PyTorch: Similar to TensorFlow, PyTorch can be used for online learning with dynamic computation graphs and custom updates.
6. MOA (Massive Online Analysis): A framework specifically designed for data stream mining and online learning tasks.
7. Apache SAMOA: A distributed streaming machine learning framework that supports online learning algorithms.
8. H2O.ai: Offers support for online learning through its machine learning platform, allowing for real-time model updates.

### Learning Rate in Online Learning:
The learning rate is a crucial hyperparameter in online learning that determines the step size at each iteration while updating the model parameters. It controls how much the model is adjusted in response to the estimated error each time the model weights are updated. A higher learning rate can lead to faster convergence but may overshoot the optimal solution, while a lower learning rate ensures more stable convergence but may require more iterations to reach the optimal solution. Selecting an appropriate learning rate is essential for the effectiveness of online learning algorithms, as it directly impacts the model's ability to learn from new data and adapt to changes in the underlying data distribution.

### Out of Core Learning:
Out of Core Learning is a technique used to train machine learning models on datasets that are too large to fit into a computer's main memory (RAM). Instead of loading the entire dataset into memory, out of core learning processes the data in smaller chunks or batches, allowing the model to learn incrementally. This approach is particularly useful for handling big data and streaming data scenarios, where the dataset size exceeds the available memory capacity. Out of core learning algorithms are designed to efficiently read, process, and update the model using these smaller data segments, enabling effective training without the need for extensive computational resources.

### Advantages of Online Learning:
1. Adaptability to New Data
2. Lower Memory Requirements
3. Real-Time Predictions        
4. Scalability
5. Cost-Effectiveness
6. Continuous Improvement
7. Efficient Use of Resources
8. Ability to Handle Concept Drift
9. Faster Model Updates
10. Flexibility in Data Processing
### Disadvantages of Online Learning:
1. Potential for Lower Accuracy
2. Sensitivity to Learning Rate
3. Risk of Overfitting Recent Data
4. Complexity in Implementation
5. Difficulty in Hyperparameter Tuning
6. Limited by Data Order
7. Challenges in Model Evaluation
8. Requires Continuous Monitoring
9. May Struggle with Noisy Data
10. Initial Model Performance May Be Poor

### Conclusion:
Both Batch Learning and Online Learning have their own advantages and disadvantages. The choice between the two approaches depends on the specific use case, data characteristics, and resource constraints. Understanding the strengths and limitations of each method is crucial for selecting the most appropriate learning strategy for a given machine learning task.

### Comparison between Batch Learning and Online Learning:
|         Offline learning       |      Features             | Online Learning|
|--------------------------------|---------------------------|----------------|
| Less complex as model is constant| Complexity    | Dynamic complexity as the model keeps evolving overtime|
| Fewer computations, single time batch-based training|Computational Power| Continuous data ingestions result in consequent model refinement computations|
| Easier to implement|Use in Production|Difficult to implement and manage|
|Image Classification or anything related to Machine learning -where data patterns remains constant without sudden concept drifts|Applications|Used in finance, economics, health where new data patterns are constantly emerging|
|Industry proven E.g. Sci-kit, Tenserflow, Pytorch,Keras, Spark Mlib|Tools|Active research/New project tools E.g. MOA, SAMOA, scikit-multiflow, stream DM|

## Day 10:
Instance Vs Model Based Learning
Instance-Based Learning:
1. Stores all training data
2. Makes predictions based on similarity to stored instances
3. Examples: k-Nearest Neighbors, Case-Based Reasoning
Model-Based Learning:
1. Builds a model from the training data
2. Makes predictions using the model
3. Examples: Linear Regression, Decision Trees

Differences:
| Aspect                 | Instance-Based Learning               | Model-Based Learning                  |
|------------------------|--------------------------------------|--------------------------------------|
| Data Storage           | Stores all training instances        | Stores a model derived from data     |
| Prediction Method      | Based on similarity to instances     | Based on the learned model           |
| Computational Cost    | High during prediction                | High during training                  |
| Adaptability           | Adapts quickly to new data           | Requires retraining for new data      |
| Examples               | k-NN, Case-Based Reasoning           | Linear Regression, Decision Trees        |    

| Instance-Based Learning               | Usual/Conventional-Based Learning                  |
|--------------------------------------|--------------------------------------|
| Prepare the data for model training|Prepare the data for model training. No difference here.|
| Train model from training data to estimate model parameters, i.e., discover patters| Do not train model. Patterns dicovery postponed until scoring query received|
|Store the model in suitable form|There is no model to store|
| Generalize the rules in form of model, even before scoring instance is seen| No generalization before scoring. Only generalize for each scoring instance individually as and when seen|
|Predict for unseen scoring instance using model|Predict for unseen scoring instance using training data directly|
|Can throw away input/training data after model training|Input/training data must be kept since each query uses part or full set of training observations|
|Requires a known model form|May not have explicit model form|
|Storing models generally requires less storage| Storing training data generally requires more storage|


Outliers in Machine Learning:
1. Definition: Data points that deviate significantly from the majority of the data.
2. Types: Point Outliers, Contextual Outliers, Collective Outliers
3. Detection Methods: Statistical Methods, Distance-Based Methods, Density-Based Methods, Clustering-Based Methods
4. Handling Outliers: Removal, Transformation, Imputation, Robust Algorithms    


## Day 11:
Day 7 of Campus X 100 Days of Machine Learning

### Type of Machine Learning:
1. Supervised Learning: Learning from labeled data (e.g., classification, regression).
2. Unsupervised Learning: Learning from unlabeled data (e.g., clustering, association
rules).
3. Semi-Supervised Learning: Combination of labeled and unlabeled data.
4. Reinforcement Learning: Learning through rewards and penalties in a dynamic environment. 
5. Self-Supervised Learning: Learning representations from the data itself without explicit labels.
6. Deep Learning: Using neural networks with multiple layers to learn complex patterns.
7. Transfer Learning: Leveraging knowledge from one task to improve learning in another related task.
8. Online Learning: Updating the model incrementally as new data arrives.
9. Batch Learning: Training the model on the entire dataset at once.
10. Active Learning: The model actively selects the most informative data points for labeling.
11. Ensemble Learning: Combining multiple models to improve performance (e.g., bagging, boosting).
12. Federated Learning: Training models across decentralized devices while keeping data localized.

### Type of Data:
1. Structured Data: Organized data in tabular format (e.g., databases, spreadsheets).
2. Unstructured Data: Data without a predefined format (e.g., text, images, audio).
3. Semi-Structured Data: Data with some organizational properties (e.g., JSON, XML).
4. Time Series Data: Data points collected or recorded at specific time intervals.
5. Categorical Data: Data that can be divided into distinct categories or groups.
6. Numerical Data: Quantitative data represented by numbers (e.g., integers, floats).
7. Text Data: Data in the form of written language (e.g., documents, social media posts).
8. Image Data: Visual data represented as pixels (e.g., photographs, medical images).
9. Audio Data: Sound data represented as waveforms (e.g., music, speech).
10. Video Data: Sequential visual data combining images and audio (e.g., movies, surveillance footage). 

### Challenges in Machine Learning:
1. Data Collection: Obtaining high-quality and relevant data.
    API or Web Scraping
2. Insufficient Data: Limited availability of labeled data for training.
    Data Augmentation
3. Non Representative Data: Training data not reflecting real-world scenarios.
    Cross-Validation
    Sampling Noise
    Sampling Bias
4. Poor Data Quality: Presence of noise, outliers, and missing values.
    Data Cleaning
5. Irrelevant Features: Inclusion of non-informative or redundant features.
    Feature Selection
    Feature Engineering
6. Overfitting: Model performs well on training data but poorly on unseen data.
    Regularization
    Cross-Validation
7. Underfitting: Model fails to capture underlying patterns in the data.
    Model Complexity
8. Software Integration: Challenges in deploying models into production environments.
    Containerization
    APIs
9. Offline Learning/Deployment: Inability to adapt to new data in real-time.
10. Cost Involved: High computational and resource costs for training and deploying models.
    Cloud Computing


Day 8 of Campus X 100 Days of Machine Learning
1. Retail and E-commerce
    During Sale they check which product to stock in using ML.
    Take phone number from user and predict which product user may buy.
    Deciding which product to show to user based on previous purchase.
2. Banking and Finance
    Fraud Detection
    Credit Scoring
    Algorithmic Trading
3. Transportation and Logistics
    Route Optimization
    Demand Prediction
    Autonomous Vehicles
4. Manufacturing
    Predictive Maintenance
    Quality Control
    Supply Chain Optimization
5. Consumer Internet Services
    Personalized Recommendations
    Content Moderation
    Search Engine Optimization
