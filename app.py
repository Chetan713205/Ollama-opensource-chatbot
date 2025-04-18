# Importing libraries
import os
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Set environment variables
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["GOOGLE_API_KEY"] = "AIzaSyD3jjlk9rl6FBUASv21T1aBAFo_h_R6rTk"  # For Gemini
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ['LANGCHAIN_PROJECT'] = "ollama_project"

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant, please respond to the questions asked."),
    ("user", "Question: {question}")
])

# Streamlit framework
st.title("Langchain demo with tinyllama (Ollama) model")
st.write("App Loaded!")

input_text = st.text_input("What question do you have in your mind?")

llm = Ollama(model="tinyllama")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(f"User Input: {input_text}")
    response = chain.invoke({"question": input_text})
    st.write("Response:")
    st.write(response)