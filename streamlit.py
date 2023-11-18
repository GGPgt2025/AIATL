import streamlit as st

# Streamlit app
st.title("Stock Pitch Deck Generator")

#Description
st.write("This program generates a basic level stock picth given a specific stock sybol..")

# User input
symbol = st.text_input("Enter Stock Symbol from S&P500 (e.g., AAPL):").upper()
