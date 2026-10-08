import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("lois_continuous.csv")

# Filter records for Swale at Catterick Bridge
swale = df[df["Unnamed: 2"] == "Swale at Catterick Bridge"]

# Convert temperature and oxygen columns to numeric
swale["Temperature water continuous"] = pd.to_numeric(
    swale["Temperature water continuous"], errors="coerce"
)

swale["Oxygen dissolved continuous"] = pd.to_numeric(
    swale["Oxygen dissolved continuous"], errors="coerce"
)

# Calculate mean temperature
mean_temp = swale["Temperature water continuous"].mean()
print("Mean Temperature:", mean_temp)

# Calculate median dissolved oxygen
median_oxygen = swale["Oxygen dissolved continuous"].median()
print("Median Dissolved Oxygen:", median_oxygen)

# Plot histogram
plt.hist(
    swale["Temperature water continuous"].dropna(),
    bins=10,
    edgecolor="black"
)

plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperature Distribution - Swale at Catterick Bridge")

plt.show()