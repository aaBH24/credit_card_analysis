import pandas as pd

df = pd.read_csv("US State Population Murder Rate.csv")

print("Population")
print("Mean:", df["Population"].mean())
print("Median:", df["Population"].median())
print("Variance:", df["Population"].var())

print("\nMurder Rate")
print("Mean:", df["Murder.Rate"].mean())
print("Median:", df["Murder.Rate"].median())
print("Variance:", df["Murder.Rate"].var())