import streamlit as st
import pandas as pd

st.title('🤖Machine Learning App')

st.write('This is app builds machine learning model!')

with st.expander('Data'):
 st.write('**Raw data**')
 df = pd.read_csv('https://raw.githubusercontent.com/sougataghosh2022-del/dp-machinelearning/refs/heads/master/Updated%20data_01_05_2025%20(1).csv')
 df
 
 X = df.drop(columns=['species'], errors='ignore')
    y = df['species'] if 'species' in df.columns else None

    st.write("X shape:", X.shape)
    if y is None:
        st.info("Target column 'species' not present after normalization.")
    else:
        st.write("y shape:", y.shape)


