import streamlit as st
import numpy as np
import pandas as pd

## Title of Streamlit
st.title("Hello Streamlit")

## Display a Simple Text
st.write("This is a simple Text")

## Create a Dataframe
df = pd.DataFrame({
    'first coloumn': [1,2,3,4],
    'second coloumn': [10,20,30,40]
})

## Display the Dataframe
st.write("Here is the Dataframe")
st.write(df)

## Create a Line Chart
chart_data=pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.line_chart()