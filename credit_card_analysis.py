import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import dataset
df = pd.read_csv("BankChurners.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# 2. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# 3. Handle missing values
# Check if any missing values exist
if df.isnull().sum().sum() == 0:
    print("\nNo missing values found in the dataset.")
else:
    # Fill numerical missing values with median
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    # Fill categorical missing values with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    print("\nMissing values handled successfully.")

# 4. Remove unnecessary columns
df.drop([
    'CLIENTNUM',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
], axis=1, inplace=True)

print("\nColumns after removing unnecessary columns:")
print(df.columns)
# 5. Plot Attrition Flag Ratio

print("\nAttrition Flag Counts:")
print(df['Attrition_Flag'].value_counts())

print("\nAttrition Flag Ratio (%):")
print(df['Attrition_Flag'].value_counts(normalize=True) * 100)

# Bar chart for Attrition Flag
plt.figure(figsize=(7, 5))

sns.countplot(x='Attrition_Flag', data=df)

plt.title("Attrition Flag Ratio")
plt.xlabel("Attrition Flag")
plt.ylabel("Number of Customers")
plt.show()
# 6. Bar Chart - Education Level

plt.figure(figsize=(8, 5))

sns.countplot(
    x='Education_Level',
    data=df,
    order=df['Education_Level'].value_counts().index
)

plt.title("Customers by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Number of Customers")
plt.xticks(rotation=45)

plt.show()


# 7. Bar Chart - Card Category

plt.figure(figsize=(7, 5))

sns.countplot(
    x='Card_Category',
    data=df
)

plt.title("Customers by Card Category")
plt.xlabel("Card Category")
plt.ylabel("Number of Customers")

plt.show()


# 8. Box Plot - Credit Limit

plt.figure(figsize=(7, 5))

sns.boxplot(y=df['Credit_Limit'])

plt.title("Box Plot of Credit Limit")
plt.ylabel("Credit Limit")

plt.show()


# 9. Box Plot - Total Transaction Amount

plt.figure(figsize=(7, 5))

sns.boxplot(y=df['Total_Trans_Amt'])

plt.title("Box Plot of Total Transaction Amount")
plt.ylabel("Total Transaction Amount")

plt.show()
# 10. Descriptive Statistics

print("\nDescriptive Statistics:")
print(df.describe())
# 11. Correlation Heatmap

# Select only numerical columns
numeric_df = df.select_dtypes(include=['int64', 'float64'])

plt.figure(figsize=(14, 10))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap")

plt.show()