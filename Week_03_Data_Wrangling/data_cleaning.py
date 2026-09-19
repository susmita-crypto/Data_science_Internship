import os
import pandas as pd

# Public Titanic dataset
csv_file = "titanic.csv"
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Load the dataset
if os.path.exists(csv_file):
    raw_df = pd.read_csv(csv_file)
else:
    raw_df = pd.read_csv(url)
    raw_df.to_csv(csv_file, index=False)

print("Raw dataset loaded successfully.")
print("Raw dataset shape:", raw_df.shape)

# Create a copy for cleaning
cleaned_df = raw_df.copy()

# Remove duplicate rows
cleaned_df = cleaned_df.drop_duplicates()

# Handle missing Age values
cleaned_df["Age"] = cleaned_df["Age"].fillna(
    cleaned_df["Age"].median()
)

# Handle missing Embarked values
cleaned_df["Embarked"] = cleaned_df["Embarked"].fillna(
    cleaned_df["Embarked"].mode()[0]
)

# Handle missing Cabin values
cleaned_df["Cabin"] = cleaned_df["Cabin"].fillna("Unknown")

# Create Family_Size feature
cleaned_df["Family_Size"] = (
    cleaned_df["SibSp"] + cleaned_df["Parch"] + 1
)

# Create Is_Alone feature
cleaned_df["Is_Alone"] = cleaned_df["Family_Size"] == 1

# Create Fare_Per_Person feature
cleaned_df["Fare_Per_Person"] = (
    cleaned_df["Fare"] / cleaned_df["Family_Size"]
)

# Create class information table
class_info = pd.DataFrame({
    "Pclass": [1, 2, 3],
    "Class_Name": [
        "First Class",
        "Second Class",
        "Third Class"
    ]
})

# Merge class information
cleaned_df = cleaned_df.merge(
    class_info,
    on="Pclass",
    how="left"
)

# Save the cleaned dataset
cleaned_df.to_csv("titanic_clean.csv", index=False)

# Final quality check
print("\nCleaning completed successfully.")
print("Final dataset shape:", cleaned_df.shape)

print("\nMissing values:")
print(cleaned_df.isnull().sum())

print("\nDuplicate rows:")
print(cleaned_df.duplicated().sum())

print("\nCleaned dataset saved as titanic_clean.csv")