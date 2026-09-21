# Capstone Project
## Customer Churn Prediction and Retention Analytics

## Project Overview

This capstone project brings together the main data science skills developed during the internship.

The project analyzes customer churn patterns, builds a machine-learning model to predict churn, evaluates the model, and communicates the findings through a business-focused dashboard and report.

## Business Question

Can customer data be used to identify customers at higher risk of churn and provide useful information for customer-retention decisions?

## Dataset

The project uses the Telco Customer Churn dataset sourced from Kaggle.

Each row represents a customer and contains demographic, service, account, charge, tenure, and churn information.

## Project Workflow

1. Define the business problem.
2. Source and inspect the dataset.
3. Clean and prepare the data.
4. Perform exploratory data analysis.
5. Visualize churn patterns.
6. Prepare features for machine learning.
7. Train a Logistic Regression model.
8. Evaluate model performance.
9. Interpret the results.
10. Create a business-focused Power BI dashboard.
11. Document limitations and future improvements.
12. Prepare the final presentation.

## Machine Learning

Logistic Regression was used as the classification model.

The preprocessing pipeline includes:

- Numerical imputation
- Numerical standardization
- Categorical imputation
- One-hot encoding

## Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix
- ROC curve

## Dashboard

A Power BI dashboard was created to communicate the main churn findings.

The dashboard includes:

- Total customers
- Churned customers
- Churn rate
- Churn rate by contract type
- Churn rate by internet service
- Churn rate by payment method
- Average customer tenure by churn status
- Average monthly charges by churn status

## Business Implication

The analysis demonstrates how customer information can be used to identify patterns associated with churn.

Churn predictions can be used as decision-support information for customer-retention activities, but predictions should not be treated as automatic business decisions.

## Limitations

The project uses one historical dataset and may not generalize to every business.

The model also has prediction errors and does not establish causal relationships.

## Future Improvements

Future work could include:

- Additional machine-learning models
- Cross-validation
- Hyperparameter tuning
- Classification threshold optimization
- External validation
- Additional business features

## Files

- `Week_12_Customer_Churn_Capstone.ipynb` — Complete capstone notebook
- `Week_12_Customer_Churn_Capstone.pbix` — Power BI dashboard
- `README.md` — Project documentation
- `data/` — Raw dataset
- `outputs/` — Dashboard data and screenshot
- `presentation/` — Final presentation

## Internship Reflection

The notebook includes a reflection on the three biggest skills learned during the internship and areas for continued improvement.