import pandas as pd

# Load the healthcare dataset
df = pd.read_csv("healthcare_dataset.csv")

# Show the first 5 patients
print(df.head())

# Basic information about the dataset

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Patient statistics

print("\nPatient Statistics:")

print("Total Patients:", len(df))

print("Average Age:", df["Age"].mean())

print("Youngest Patient:", df["Age"].min())

print("Oldest Patient:", df["Age"].max())

print("\nGender Distribution:")
print(df["Gender"].value_counts())

print("\nMedical Condition Distribution:")
print(df["Medical Condition"].value_counts())

# Healthcare details analysis

print("\nAdmission Type Distribution:")
print(df["Admission Type"].value_counts())

print("\nTest Results Distribution:")
print(df["Test Results"].value_counts())

print("\nMedication Distribution:")
print(df["Medication"].value_counts())

print("\nInsurance Provider Distribution:")
print(df["Insurance Provider"].value_counts())

# Billing and hospital analysis

print("\nBilling Statistics:")
print("Average Billing Amount:", df["Billing Amount"].mean())
print("Minimum Billing Amount:", df["Billing Amount"].min())
print("Maximum Billing Amount:", df["Billing Amount"].max())

print("\nHospital Distribution:")
print(df["Hospital"].value_counts().head(10))

# Data Visualizations

import matplotlib.pyplot as plt

# 1. Gender Distribution
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")
plt.show()

# 2. Medical Condition Distribution
df["Medical Condition"].value_counts().plot(kind="bar")
plt.title("Medical Condition Distribution")
plt.xlabel("Medical Condition")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.show()

# 3. Admission Type Distribution
df["Admission Type"].value_counts().plot(kind="bar")
plt.title("Admission Type Distribution")
plt.xlabel("Admission Type")
plt.ylabel("Number of Patients")
plt.show()

# 4. Test Results Distribution
plt.figure()
df["Test Results"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Test Results Distribution")
plt.ylabel("")
plt.show()
plt.close()

# 5. Medication Distribution
plt.figure()
df["Medication"].value_counts().plot(kind="bar")
plt.title("Medication Distribution")
plt.xlabel("Medication")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.show()
plt.close()

# 6. Age Distribution
plt.figure()
df["Age"].plot(kind="hist", bins=10)
plt.title("Patient Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.show()
plt.close()