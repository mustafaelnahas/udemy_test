# importing libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(layout='centered')


st.title("Udemy Courses EDA")
st.text("This is our first challenging dashboard!\nYAY! *_*")

st.write("Credits: @MustafaOthman")

# loading data
df = pd.read_csv('udemy_courses.csv')
st.dataframe(df.head())

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader('How many courses in each subject?')
    fig = px.bar(data_frame=df ,x=df['subject'])
    st.plotly_chart(fig)
    # st.text("In this chart we are trying to help ahmed to relax")

with col2:
    st.subheader('What is the average price for each subject?')
    dic = dict(df.groupby('subject').mean()['price'])
    fig = px.bar(data_frame=df, x=dic.keys(), y=dic.values())
    fig.update_xaxes(title='Subject')
    fig.update_yaxes(title='Average Price')
    st.plotly_chart(fig)

st.subheader('How many courses for each subject regarding: (paid/unpaid | level)?')
option = st.selectbox("Select an option",['is_paid','level'])
fig = px.bar(data_frame=df, x=df['subject'], color=option)
st.plotly_chart(fig)
