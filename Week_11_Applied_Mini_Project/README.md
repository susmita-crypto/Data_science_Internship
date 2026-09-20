# Week 11 — Applied Mini Project: Customer Churn Prediction

## Project Overview

This project applies the data science techniques developed during the internship to a practical customer churn prediction problem.

The project covers the complete workflow from raw data to business interpretation:

- Data loading
- Data inspection
- Data cleaning
- Exploratory Data Analysis
- Data visualization
- Feature preprocessing
- Machine learning
- Model evaluation
- Business interpretation

## Business Question

Which customer characteristics are associated with customer churn, and can a machine-learning model predict whether a customer is likely to leave the company?

## Dataset

The project uses the Telco Customer Churn dataset downloaded from Kaggle.

Each row represents a customer and includes information about customer demographics, services, account information, charges, and churn status.

## Tools and Libraries

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

1. Load the raw dataset.
2. Inspect the dataset structure.
3. Clean data types and missing values.
4. Remove the customer identifier.
5. Explore customer churn patterns.
6. Prepare numerical and categorical features.
7. Split the data into training and testing sets.
8. Train a Logistic Regression model.
9. Evaluate the model using multiple classification metrics.
10. Interpret the model results.
11. Explain the business implications in plain language.

## Machine Learning Model

A Logistic Regression classifier is used because the target variable is binary:

- `0` = No churn
- `1` = Churn

The preprocessing pipeline includes:

- Median imputation for numerical missing values
- Standardization of numerical features
- Most-frequent imputation for categorical variables
- One-hot encoding of categorical variables

## Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix
- ROC curve

## Business Implication

The analysis demonstrates how customer information can be used to identify patterns associated with churn and develop a model that estimates churn risk.

In a real business environment, such predictions could support customer-retention activities. However, predictions should be treated as decision-support information rather than automatic decisions.

## Limitations

The findings are based on a single historical dataset and may not generalize to every business.

The model identifies statistical associations but does not establish causal relationships. It may also produce false-positive and false-negative predictions.

## Mentor Feedback

Initial mentor feedback is pending and will be incorporated after review.

## Files

- `Week_11_Customer_Churn.ipynb` — Complete project notebook
- `data/WA_Fn-UseC_-Telco-Customer-Churn.csv` — Raw dataset