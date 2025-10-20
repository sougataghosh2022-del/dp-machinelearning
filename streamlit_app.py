import streamlit as st
import pandas as pd

st.title('🤖Machine Learning App')

st.write('This is app builds machine learning model!')

with st.expander('Data'):
 st.write('**Raw data**')
 df = pd.read_csv('https://raw.githubusercontent.com/sougataghosh2022-del/dp-machinelearning/refs/heads/master/Updated%20data_01_05_2025%20(1).csv')
 df

st.write('**X**')
X = df.drop('label', axis=1)
X
st.write('**Y**')
Y = df.label
Y

# ✅ Corrected code for your dataset to fix the IndentationError and wrong column names

with st.expander("Data visualization"):
    # Your dataset does NOT have 'bill_length_mm', 'body_mass_9', or 'species'
    # So we use valid columns from your uploaded dataset
    df.columns = df.columns.str.strip().str.lower()

    # Select any two numeric columns from the dataset for plotting
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if "label" in df.columns and len(numeric_cols) >= 2:
        st.scatter_chart(data=df, x=numeric_cols[0], y=numeric_cols[1], color="label")
    else:
        st.warning("Not enough numeric data to display scatter chart.")








 
 

