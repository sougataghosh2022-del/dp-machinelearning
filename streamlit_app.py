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

with st.expander('Data visualization'):
with st.container():
    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # Get numeric columns (skip 'label')
    numeric_cols = df.columns[1:]

    # Column selection UI
    x_axis = st.selectbox("Select X-axis column", numeric_cols, index=0)
    y_axis = st.selectbox("Select Y-axis column", numeric_cols, index=1)

    # Scatter chart
    st.write(f"### Scatter Chart: {x_axis} vs {y_axis}")
    st.scatter_chart(
        data=df,
        x=x_axis,
        y=y_axis,
        color='label'
    )









 
 

