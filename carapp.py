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





# Separate numerical and categorical columns
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Streamlit app setup
st.title("Data Visualization App")

# Heatmap Section
viz_type = st.selectbox("Select Visualization Type", ["Heatmap", "Other"])
if viz_type == "Heatmap":
    st.write("### Heatmap")
    
    # Select columns for heatmap
    index_col = st.selectbox("Select Index column", numerical_cols)
    columns_col = st.selectbox("Select Columns column", numerical_cols)
    values_col = st.selectbox("Select Values column", numerical_cols)
    
    # Check if valid columns are selected
    if index_col and columns_col and values_col:
        # Pivot the data for heatmap
        pivot_df = df.pivot_table(index=index_col, columns=columns_col, values=values_col, aggfunc='mean')
        
        # Plot the heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(pivot_df, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title(f"Heatmap: {values_col} by {index_col} and {columns_col}")
        st.pyplot(plt)

    
    try:
        # Ensure the values column is numeric for heatmap
        if pd.api.types.is_numeric_dtype(df[values_col]):
            # Ensure index and columns are categorical
            if pd.api.types.is_numeric_dtype(df[index_col]) and index_col != 'symboling':
                st.error(f"The Index column '{index_col}' should be categorical. Please select a categorical column.")
            elif pd.api.types.is_numeric_dtype(df[columns_col]) and columns_col != 'symboling':
                st.error(f"The Columns column '{columns_col}' should be categorical. Please select a categorical column.")
            else:
                # Handle duplicates by aggregating with mean
                pivot_table = df.pivot_table(index=index_col, columns=columns_col, values=values_col, aggfunc='mean')
                
                # Plot the heatmap
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="RdBu", ax=ax)
                st.pyplot(fig)
        else:
            st.error(f"Heatmap requires numeric data for the '{values_col}' column. Please select a numeric column for the values.")
    except Exception as e:
        st.error(f"Error creating heatmap: {e}")

elif viz_type == "Boxplot":
    st.write("### Boxplot")
    x_col = st.selectbox("Select X-axis column", df.columns)
    y_col = st.selectbox("Select Y-axis column", df.columns)

    try:
        # Ensure the Y-axis column is numeric for boxplot
        if pd.api.types.is_numeric_dtype(df[y_col]):
            fig, ax = plt.subplots()
            sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)
            st.pyplot(fig)
        else:
            st.error(f"Boxplot requires numeric data for the Y-axis. The selected column '{y_col}' is not numeric.")
    except Exception as e:
        st.error(f"Error creating boxplot: {e}")
