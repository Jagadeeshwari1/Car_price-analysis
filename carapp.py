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

# Convert 'symboling' column to categorical type
df['symboling'] = df['symboling'].astype('category')

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



elif viz_type == "Boxplot":
    st.write("### Boxplot")
    x_col = st.selectbox("Select X-axis column", df.columns)
    y_col = st.selectbox("Select Y-axis column", df.columns)
    try:
        if pd.api.types.is_numeric_dtype(df[y_col]):
            fig, ax = plt.subplots()
            sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)
            st.pyplot(fig)
        else:
            st.error("Boxplot requires numeric data for the Y-axis.")
    except Exception as e:
        st.error(f"Error creating boxplot: {e}")
