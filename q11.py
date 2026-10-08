import pandas as pd

# Create dataset
data = {
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Salary": [50000, 55000, 45000, 48000, 40000, 42000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Pivot Table
pivot = pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)

print("\nPivot Table:")
print(pivot)

# Cross Tabulation
cross_tab = pd.crosstab(
    df["Department"],
    df["Gender"]
)

print("\nCross Tabulation:")
print(cross_tab)