import matplotlib.pyplot as plt

# Heights of classmates in cm
heights = [150, 155, 160, 162, 158, 170, 165, 172,
           168, 155, 160, 164, 175, 180, 170, 166,
           159, 163, 171, 167]

# Histogram
plt.hist(heights, bins=5, edgecolor="black")

plt.xlabel("Height (cm)")
plt.ylabel("Number of Students")
plt.title("Distribution of Students' Heights")

plt.show()