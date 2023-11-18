import streamlit as st

# Streamlit app
st.title("Stock Pitch Deck Generator")

# User input
symbol = st.text_input("Enter Stock Symbol from S&P500 (e.g., AAPL):").upper()