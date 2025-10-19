# Mini Project : Data Summary

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv('data.csv')

# Basic Information
print("Data Overview")
print(data.info())
print("\n")

# First Few Rows:
print("Sample DAta")
print(data.head())
print("\n")

# Descriptive Statistics
print("Summary Statistics")
print(data.describe())
print("\n")

# Check for missing values
print("Missing Values")
print(data.isnull().sum())
print("\n")

# Correlation Matrix
print("Correlation Matrix")
print(data.corr(numeric_only=True))
print("\n")

# Visulaization Example
#Histogram for numeric columns
data.hist(figsize=(10,8))
plt.suptitle("Data distribution")
plt.show()

# Correlation heatmap(Optional, if seaborn is available)
try:
    import seaborn as sns
    plt.figure(figsize=(8,6))
    sns.heatmap(data.corr(numeric_only=True),annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()
except ImportError:
    print("Install seaborn to see correlation heatmap: pip3 install seaborn")

# Save Summary Report
summary = {
    "shape": data.shape,
    "missing_values": data.isnull().sum().to_dict(),
    "columns":list(data.columns),
    "summary_stats": data.describe().to_dict(),
}
pd.Series(summary).to_json("data_summary.json",indent=4)
print("Summary report saved as data_summary.json")