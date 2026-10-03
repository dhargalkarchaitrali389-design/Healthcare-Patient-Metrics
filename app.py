import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("healthcare_dataset.csv")

# Page title
st.title("🏥 Healthcare Patient Metrics Dashboard")
st.write("Interactive analysis of healthcare patient data")

# Sidebar
st.sidebar.header("🔎 Filters")

# Gender filter
gender_options = ["All"] + sorted(df["Gender"].unique().tolist())
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

# Apply filter
if selected_gender != "All":
    filtered_df = df[df["Gender"] == selected_gender]
else:
    filtered_df = df

# Patient overview
st.subheader("📊 Patient Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", len(filtered_df))
col2.metric("Average Age", round(filtered_df["Age"].mean(), 1))
col3.metric("Average Billing", round(filtered_df["Billing Amount"].mean(), 2))

# Medical condition
st.subheader("🩺 Medical Condition Distribution")
st.bar_chart(filtered_df["Medical Condition"].value_counts())

# Admission type
st.subheader("🏥 Admission Type Distribution")
st.bar_chart(filtered_df["Admission Type"].value_counts())

# Test results
st.subheader("🧪 Test Results Distribution")
st.bar_chart(filtered_df["Test Results"].value_counts())

# Medication
st.subheader("💊 Medication Distribution")
st.bar_chart(filtered_df["Medication"].value_counts())

# Age
st.subheader("🎂 Age Distribution")
st.bar_chart(filtered_df["Age"].value_counts().sort_index())