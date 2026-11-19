
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="AI Data Analytics", layout="wide")

# Title
st.title("AI-Powered Data Analytics")
st.write("Welcome to your first Data Analytics Project!")

# Upload CSV File
uploaded_file = st.file_uploader(
    "Upload your CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    # Read Dataset
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Dataset Information
    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    # Statistical Summary
    st.subheader("Statistical Summary")
    st.write(df.describe())

    # Data Visualization
    st.subheader("Data Visualization")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if numeric_columns:

        selected_column = st.selectbox(
            "Select a column",
            numeric_columns
        )

        # Histogram
        st.write("Distribution of Selected Column")

        fig, ax = plt.subplots()
        sns.histplot(df[selected_column].dropna(), kde=True, ax=ax)
        ax.set_title(f"Distribution of {selected_column}")
        st.pyplot(fig)

        # Correlation Heatmap
        st.subheader("Correlation Heatmap")

        if len(numeric_columns) >= 2:
            fig, ax = plt.subplots()
            sns.heatmap(
                df[numeric_columns].corr(),
                annot=True,
                cmap="coolwarm",
                ax=ax
            )
            st.pyplot(fig)
        else:
            st.info("At least two numerical columns are needed for a heatmap.")

    else:
        st.warning("No numerical columns found in this dataset.")

    # Automatic Insights
    st.subheader("Data Insights")

    st.write(f"Your dataset contains **{df.shape[0]} rows** and **{df.shape[1]} columns**.")

    st.write(f"Total missing values: **{df.isnull().sum().sum()}**")

    if numeric_columns:
        for column in numeric_columns:
            st.write(
                f"Average {column}: **{df[column].mean():.2f}**"
            )

    st.success("Data Analysis Completed Successfully!")

else:
    st.info("Please upload a CSV file to begin data analysis.")
