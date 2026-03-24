import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Age": [20, 22, 23, 21, 24, 22, 23],
    "Height": [160, 165, 170, 158, 172, 168, 169],
    "Gender": ["F", "M", "M", "F", "M", "F", "M"]
}

df = pd.DataFrame(data)

print("Variable Types:")
print(df.dtypes)
print()

print("Summary Statistics:")
print(df.describe())
print()

plt.figure()
plt.hist(df["Age"], bins=5, color="pink", edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Age")
plt.show()

plt.figure()
plt.scatter(df["Age"], df["Height"], color="pink")
plt.xlabel("Age")
plt.ylabel("Height")
plt.title("Age vs Height")
plt.show()

gender_counts = df["Gender"].value_counts()

plt.figure()
plt.bar(gender_counts.index, gender_counts.values, color="pink", edgecolor="black")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Gender Distribution")
plt.show()
