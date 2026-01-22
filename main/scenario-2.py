import pandas as pd
import matplotlib.pyplot as plt

# 2) Load the dataset (place CSV in your working folder)
df = pd.read_csv("diabetes.csv")

# 3) Explore data structure
print("HEAD:\n", df.head())
print("\nINFO:")
df.info()
print("\nDESCRIBE:\n", df.describe())

# 4) Check for missing values
# (Note: In this dataset, zeros indicate missing values for some health metrics)
print("\nMissing Values:\n", df.isnull().sum())
print("\nZero Values (treated as missing):\n")
print((df == 0).sum())

# 5) Visualize glucose levels (Histogram)
plt.figure()
plt.hist(df["Glucose"], bins=20)
plt.title("Glucose Level Distribution")
plt.xlabel("Glucose")
plt.ylabel("Frequency")
plt.show()

# 6) Visualize age distribution (Histogram)
plt.figure()
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 7) Boxplot for glucose levels
plt.figure()
plt.boxplot(df["Glucose"])
plt.title("Boxplot of Glucose Levels")
plt.ylabel("Glucose")
plt.show()

# 8) Boxplot for age
plt.figure()
plt.boxplot(df["Age"])
plt.title("Boxplot of Age")
plt.ylabel("Age")
plt.show()

# 9) Basic pattern identification
print("\nObservations:")
print("- Zero values in Glucose, BloodPressure, SkinThickness, Insulin, and BMI indicate missing data.")
print("- Glucose shows wide spread and outliers, linked to diabetes risk.")
print("- Age distribution is right-skewed, with more patients in younger age groups.")