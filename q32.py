import matplotlib.pyplot as plt

# Areas of continents in million square kilometres
continents = ["Asia", "Africa", "North America", "South America",
              "Antarctica", "Europe", "Australia"]

area = [44.58, 30.37, 24.71, 17.84, 14.20, 10.18, 8.53]

# Bar chart
plt.bar(continents, area)

plt.xlabel("Continents")
plt.ylabel("Area (million sq. km)")
plt.title("Areas of Continents")

plt.xticks(rotation=45)
plt.show()