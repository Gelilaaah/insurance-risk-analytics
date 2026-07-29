import streamlit as st
import pandas as pd
import plotly.express as px


st.title("📈 Exploratory Data Analysis")


# Load data

df = pd.read_csv(
    "data/processed/MachineLearningRating_v3.csv"
)


st.subheader("Dataset Preview")


st.dataframe(
    df.head()
)


st.subheader("Dataset Information")


col1, col2 = st.columns(2)


with col1:
    st.metric(
        "Rows",
        df.shape[0]
    )


with col2:
    st.metric(
        "Columns",
        df.shape[1]
    )



st.subheader("Missing Values")


missing = (
    df.isnull()
    .sum()
    .reset_index()
)


missing.columns = [
    "Column",
    "Missing Values"
]


fig = px.bar(
    missing,
    x="Column",
    y="Missing Values",
    title="Missing Data"
)


st.plotly_chart(fig)

st.subheader("Numerical Distribution")


numeric_columns = df.select_dtypes(
    include="number"
).columns


selected_column = st.selectbox(
    "Choose a variable",
    numeric_columns
)


fig = px.histogram(
    df,
    x=selected_column,
    bins=50,
    title=f"Distribution of {selected_column}"
)


st.plotly_chart(fig)