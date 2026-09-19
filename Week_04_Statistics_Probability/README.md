# Statistics and Probability Basics

## Objective

This week focused on understanding basic statistics and probability concepts and applying descriptive statistics to a new real-world dataset.

## Topics Covered

- Mean
- Median
- Mode
- Variance
- Standard deviation
- Correlation
- Basic probability
- Conditional probability
- Normal distribution
- Central Limit Theorem

## Mini Project

For the mini project, I selected the Students Performance dataset.

The analysis included:

1. Loading and exploring the dataset
2. Checking the dataset structure and data types
3. Checking for missing values
4. Checking for duplicate rows
5. Cleaning and standardizing column names
6. Saving the cleaned dataset
7. Calculating descriptive statistics
8. Performing correlation analysis
9. Creating visualizations
10. Writing statistical findings and conclusions

## Dataset

The dataset contains 1,000 student records and 8 variables:

- Gender
- Race/ethnicity
- Parental level of education
- Lunch
- Test preparation course
- Math score
- Reading score
- Writing score

Source:

https://github.com/sharmaroshan/Students-Performance-Analytics

## Data Cleaning Results

- Rows: 1,000
- Columns: 8
- Missing values: 0
- Duplicate rows: 0
- Numerical score columns stored as integers
- Column names standardized using lowercase letters and underscores

## Key Statistical Findings

The average scores were:

- Mathematics: 66.09
- Reading: 69.17
- Writing: 68.05

Reading had the highest average score.

The correlations between the subjects were positive:

- Math and Reading: approximately 0.82
- Math and Writing: approximately 0.80
- Reading and Writing: approximately 0.95

The strongest relationship was between reading and writing scores.

Correlation shows an association between variables and does not by itself establish causation.

## Files

- `Week_04_Statistics_Probability.ipynb` — Main analysis notebook
- `StudentsPerformance_clean.csv` — Cleaned dataset
- `data/StudentsPerformance.csv` — Original downloaded dataset
- `README.md` — Week 4 documentation

## Learning Outcome

This week helped me understand how statistical measures can summarize numerical data and how correlation can be used to examine relationships between variables.

I also practiced applying statistics and probability concepts to a new dataset and communicating the results in a clear written format.