import streamlit as st
from analysis.analyze_10k import analyze_10k
from analysis.analyze_yahoo import fetch_stock_data

st.title("Stock Pitch Deck Generator")

# User input
symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):").upper()

# Fetch real-time stock data
stock_data = fetch_stock_data()

# if stock_data:
#     st.subheader("Real-Time Stock Data:")
#     st.write(f"Symbol: {symbol}")
#     st.write(f"Current Price: {stock_data['c']}")

#     # Fetch 10-K data (replace this with actual data fetching logic)
#     ten_k_text = fetch_10k_data(symbol)

#     # Analyze 10-K data
#     if ten_k_text:
#         analysis_result = analyze_10k(ten_k_text)
#         display_results(analysis_result)
#     else:
#         st.warning("Failed to fetch 10-K data. Please check the symbol.")
# else:
#     st.warning("Failed to fetch real-time stock data. Please check the symbol or try again later.")