import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get the API key from the environment variable
api_key = os.environ.get("GROQ_API_KEY")

# Initialize the Groq LLM with the loaded API key
api_key = "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"
if api_key:
    llm = ChatGroq(
        api_key=api_key,
        model="mixtral-8x7b-32768",  # specify the model explicitly
        temperature=0.7,
    )
    print("LLM successfully initialized")
else:
    print("Failed to load LLM: API key might be missing.")


#Function of main script
pandas_agent = create_pandas_dataframe_agent(llm, df, verbose=True, allow_dangerous_code=True)
    # Now you can ask questions about the DataFrame
def function_agent():
        st.write("**Data Overview**")
        st.write("The first rows of your dataset look like this:")
        st.write(df.head())
        st.write("**Data Cleaning**")
        columns_df = pandas_agent.run("What are the meaning of the columns?")
        st.write(columns_df)
        missing_values = pandas_agent.run("How many missing values does this dataframe have? Start the answer with 'There are'")
        st.write(missing_values)
        duplicates = pandas_agent.run("Are there any duplicate values and if so where?")
        st.write(duplicates)
        st.write("**Data Summarisation**")
        st.write(df.describe())
        correlation_analysis = pandas_agent.run("Calculate correlations between numerical variables to identify potential relationships.")
        st.write(correlation_analysis)
        outliers = pandas_agent.run("Identify outliers in the data that may be erroneous or that may have a significant impact on the analysis.")
        st.write(outliers)
        new_features = pandas_agent.run("What new features would be interesting to create?.")
        st.write(new_features)
        return
# Main body
st.title('AI Assistance for Data Science')
st.write('Hello, I\'m your AI Assistant and I am here to help you with your Data Science Projects.')

# Initialize the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1: False}

# Function to update value in sessions
def clicked(button):
    st.session_state.clicked[button] = True

st.button("Let's get started", on_click=clicked, args=[1])
if st.session_state.clicked[1]:
    st.header("Exploratory Data Analysis")
    st.subheader('Solution')

    # User upload the file
    user_csv = st.file_uploader("Upload your file here", type="csv")
    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)

# Integrate the LLM
with st.sidebar:
        with st.expander('What are the steps of EDA'):
            with st.spinner("Getting response from the LLM..."):
                try:
                    # Create a chat message for the system and user interaction
                    messages = [
                        ("system", "You are a data science expert."),
                        ("user", "What are the steps of EDA?")
                    ]
                    # Use the LLM to respond to the query
                    response = llm.invoke(messages)
                    st.write(response.content)  # Display the LLM's response
                except Exception as e:
                    st.error(f"Failed to get response from LLM: {e}")
    



function_agent()
