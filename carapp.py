import streamlit as st
import pandas as pd

# Attempt to import matplotlib and seaborn
try:
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError as e:
    st.error(f"An import error occurred: {e}. Please ensure the required libraries are installed by running:")
    st.code("pip install matplotlib seaborn pandas", language="bash")
    st.stop()

# App Title
st.title("Visualization Dashboard")

# Load dataset directly from the provided URL
uploaded_file = "https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv"

try:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")
except Exception as e:
    st.error(f"Error loading the dataset from the provided URL: {e}")
    st.stop()

# Display dataset overview
st.write("### Dataset Overview")
st.dataframe(df)

# Visualization selection
viz_type = st.selectbox("Choose a visualization type", ["Scatter Plot", "Heatmap", "Boxplot"])

if viz_type == "Scatter Plot":
    st.write("### Scatter Plot")
    x_col = st.selectbox("Select X-axis column", df.columns)
    y_col = st.selectbox("Select Y-axis column", df.columns)
    try:
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error creating scatter plot: {e}")

elif viz_type == "Heatmap":
    st.write("### Heatmap")
    index_col = st.selectbox("Select Index column", df.columns)
    columns_col = st.selectbox("Select Columns column", df.columns)
    values_col = st.selectbox("Select Values column", df.columns)
    try:
        if pd.api.types.is_numeric_dtype(df[values_col]):
            # Handle duplicate entries by aggregating with mean
            grouped = df.groupby([index_col, columns_col])[values_col].mean().reset_index()
            pivot_table = grouped.pivot(index=index_col, columns=columns_col, values=values_col)
            
            # Plot the heatmap
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="RdBu", ax=ax)
            st.pyplot(fig)
        else:
            st.error("Heatmap requires numeric data for the Values column.")
    except Exception as e:
        st.error(f"Error creating heatmap: {e}")

elif viz_type == "Boxplot":
    st.write("### Boxplot")
    x_col = st.selectbox("Select X-axis column", df.columns)
    y_col = st.selectbox("Select Y-axis column", df.columns)
    try:
        if pd.api.types.is_numeric_dtype(df[y_col]):
            fig, ax = plt.subplots()
            sns.boxplot(data=df, x
