# Streamlit Visualization Dashboard

This repository contains a Streamlit-based data visualization web app built using the cleaned automobile dataset. It allows users to interactively explore the data with scatter plots, heatmaps, and boxplots.

## 📊 App Features

- **Scatter Plot**: Choose any two columns for the X and Y axes to view their relationships.
- **Heatmap**: Pivot the dataset based on selected index, columns, and values to create a heatmap.
- **Boxplot**: Analyze distribution of numeric values across categorical variables.

## 🗂️ Dataset Used

The app uses a public dataset hosted on GitHub:
- [CleanedAutomobile.csv](https://raw.githubusercontent.com/klamsal/Fall2024Exam/refs/heads/main/CleanedAutomobile.csv)

## ▶️ How to Run the App

Ensure Python is installed along with the required libraries:

```bash
pip install streamlit pandas matplotlib seaborn
```

Then run the app:

```bash
streamlit run app.py
```

> Make sure your script file is named `app.py` or update the command accordingly.

## 📌 Notes

- The dataset is loaded directly from an online URL.
- Categorical handling and validation are included for accurate plotting.
- Duplicate entries in heatmap data are handled using aggregation (mean).

## 👩‍💻 Author

**Jagadishwari**  
Master's Student in Applied Analytics  
Saint Louis University
