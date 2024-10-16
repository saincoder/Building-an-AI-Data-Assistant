import streamlit as st
import pandas as pd
import os

from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#Main body
st.title('AI Assisance for Data Science')
st.write('Hello, Im your AI Assistant and I am here to help you with your Data Science Projects.')


#Intialize the key n session state
if 'clicked' not in st.session_state:
    st.session_state.clicked={1:False}

#function to update value in sessions
def clicked(button):
    st.session_state.clicked[button]=True

if st.button("Let's get started"):
    st.header("Exploraty Data Analysis")
    st.subheader('Solution')
    user_csv = st.file_uploader("Upload your file here", type="csv")