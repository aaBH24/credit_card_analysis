import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("BankChurners.csv")

# Bar chart of Attrition Flag
df["Attrition_Flag"].value_counts().plot(kind="bar")

plt.xlabel("Attrition Flag")
plt.ylabel("Number of Customers")
plt.title("Customer Attrition")

plt.show()


# Bar chart of Gender
df["Gender"].value_counts().plot(kind="bar")

plt.xlabel("Gender")
plt.ylabel("Number of Customers")
plt.title("Gender Distribution")

plt.show()


# Box plot of Customer Age
sns.boxplot(x=df["Customer_Age"])

plt.title("Box Plot of Customer Age")

plt.show()


# Correlation heatmap
numeric_df = df.select_dtypes(include="number")

sns.heatmap(numeric_df.corr(), annot=True)

plt.title("Correlation Heatmap")

plt.show()