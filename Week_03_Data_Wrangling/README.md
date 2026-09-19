\# Week 3 - Data Wrangling with NumPy and Pandas



\## Objective



The objective of Week 3 is to learn how to use NumPy and Pandas for numerical computing and data wrangling.



\## Topics Covered



\### NumPy



\- Array creation

\- Array indexing

\- Broadcasting

\- Vectorized operations



\### Pandas



\- Loading a public CSV dataset

\- Exploring dataset structure

\- Checking missing values

\- Handling missing values

\- Removing duplicate rows

\- Filtering rows

\- GroupBy operations

\- Merging DataFrames

\- Creating new columns

\- Saving cleaned data



\## Dataset



The Titanic public CSV dataset was used for the Pandas data-wrangling exercises.



The raw dataset contains 891 rows and 12 columns.



The cleaned dataset contains 891 rows and 16 columns after cleaning and feature creation.



\## Data Cleaning



The following cleaning steps were performed:



1\. Loaded the public Titanic dataset.

2\. Checked the dataset structure and missing values.

3\. Removed duplicate rows.

4\. Filled missing `Age` values using the median.

5\. Filled missing `Embarked` values using the mode.

6\. Filled missing `Cabin` values with `"Unknown"`.

7\. Created `Family\_Size`.

8\. Created `Is\_Alone`.

9\. Created `Fare\_Per\_Person`.

10\. Merged passenger class information using a separate DataFrame.

11\. Performed a final data-quality check.

12\. Saved the cleaned dataset.



\## Final Data Quality



The final dataset has:



\- 891 rows

\- 16 columns

\- 0 missing values

\- 0 duplicate rows



\## Files



&#x20;File Description 

&#x20;`Week\_03\_Data\_Wrangling.ipynb`- Main Week 3 notebook 

&#x20;`titanic.csv` - Raw Titanic dataset 

&#x20;`titanic\_clean.csv` - Cleaned analysis-ready dataset 

&#x20;`data\_cleaning.py` - Reusable data-cleaning script 

&#x20;`README.md` - Week 3 documentation 



\## How to Run



1\. Open Jupyter Notebook or JupyterLab.

2\. Open `Week\_03\_Data\_Wrangling.ipynb`.

3\. Run the notebook cells from top to bottom.

4\. Review the raw dataset and cleaning steps.

5\. Check the final data-quality results.

6\. Run `data\_cleaning.py` with Python to reproduce the cleaning process.



\## Learning Outcome



After completing Week 3, I can use NumPy for basic numerical operations and Pandas for loading, cleaning, transforming, merging, and preparing tabular data for analysis.

