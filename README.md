# Titanic Survival Prediction

## Logistic Regression Analysis and Deployment for Survival Prediction
### Objective:
This repository focuses on performing a logistic regression analysis to predict survival probabilities based on given features. The project encompasses data exploration, preprocessing, model building, evaluation, and deployment using Streamlit.

## Tasks and Workflow

### Data Exploration
- Loading and EDA: Load the dataset and perform exploratory data analysis (EDA) to understand its structure.
- Feature Examination: Review feature types and summary statistics to gain insights into the data.
- Visualizations: Create visualizations including histograms, box plots, and pair plots to explore feature distributions and relationships. Analyze observed patterns and 
  correlations.

### Data Preprocessing
- Handling Missing Values: Address missing values using appropriate imputation techniques.
- Encoding Categorical Variables: Convert categorical variables into numerical formats suitable for logistic regression.

### Model Building
- Logistic Regression Model: Develop a logistic regression model using libraries such as scikit-learn.
- Training: Train the model using the training dataset to learn the relationship between features and the target variable.

### Model Evaluation
- Performance Metrics: Evaluate the model’s performance on the testing dataset using accuracy, precision, recall, F1-score, and ROC-AUC score.
- ROC Curve: Visualize the ROC curve to assess the model’s performance across different classification thresholds.

### Interpretation
- Coefficient Interpretation: Interpret the coefficients of the logistic regression model to understand the impact of each feature on the target variable.
- Feature Significance: Discuss the significance of various features in predicting survival probability.

### Deployment with Streamlit
- Streamlit App: Deploy the logistic regression model using Streamlit to create an interactive web application.
- User Interface: Develop a Streamlit app that allows users to input data and receive survival predictions from the trained model. The app can be deployed locally or online 
  via Streamlit Share.
