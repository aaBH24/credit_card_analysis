import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company-sales.csv")
# Q34(a)
plt.figure()
plt.plot(df["month_number"], df["total_profit"])
plt.show()


# Q34(b)
plt.figure()
plt.plot(df["month_number"], df["total_profit"],
         linestyle="--", marker="o")
plt.show()


# Q34(c)
plt.figure()
plt.plot(df["month_number"], df["facecream"], label="Face Cream")
plt.plot(df["month_number"], df["facewash"], label="Face Wash")
plt.plot(df["month_number"], df["toothpaste"], label="Toothpaste")
plt.legend()
plt.show()

#(d)
plt.figure()
plt.scatter(df["month_number"], df["total_units"])

plt.xlabel("Month")
plt.ylabel("Total Units Sold")
plt.title("Total Units Sold per Month")

plt.show()

#(e)
plt.figure()
plt.bar(df["month_number"], df["total_profit"])

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit per Month")

plt.show()

#f
plt.figure()
plt.bar(df["month_number"], df["total_profit"])

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit per Month")

plt.savefig("total_profit.png")

plt.show()

#g
plt.figure()
plt.hist(df["total_profit"], bins=5, edgecolor="black")

plt.xlabel("Total Profit")
plt.ylabel("Frequency")
plt.title("Distribution of Total Profit")

plt.show()

#h
plt.figure()
products = ["Face Cream", "Face Wash", "Toothpaste",
            "Bathing Soap", "Shampoo", "Moisturizer"]

sales = [
    df["facecream"].sum(),
    df["facewash"].sum(),
    df["toothpaste"].sum(),
    df["bathingsoap"].sum(),
    df["shampoo"].sum(),
    df["moisturizer"].sum()
]

plt.pie(sales, labels=products, autopct="%1.1f%%")

plt.title("Total Product Sales")

plt.show()

#i
plt.figure()
plt.subplot(2, 1, 1)

plt.plot(df["month_number"], df["total_profit"])
plt.title("Total Profit")

plt.subplot(2, 1, 2)

plt.bar(df["month_number"], df["total_units"])
plt.title("Total Units Sold")

plt.tight_layout()

plt.show()

#j
plt.figure()
months = df["month_number"]

plt.stackplot(
    months,
    df["facecream"],
    df["facewash"],
    df["toothpaste"],
    labels=["Face Cream", "Face Wash", "Toothpaste"]
)

plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.title("Product Sales - Stack Plot")

plt.legend(loc="upper left")

plt.show()