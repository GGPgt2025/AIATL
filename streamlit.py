# import streamlit as st
# from analysis.analyze_10k import analyze_10k, fetch_10k_data
# from analysis.analyze_yahoo import fetch_stock_data

# st.title("Stock Pitch Deck Generator")

# # User input
# symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):").upper()

# if st.button("Generate Stock Pitch"):
#     if symbol:
#         # st.subheader("Real-Time Stock Data:")
#         st.write(f"Symbol: {symbol}")
#         # st.write(f"Current Price: {stock_data['c']}")
#         # Fetch 10-K data
#         html_content = fetch_10k_data(symbol)
        
#         if html_content:
#             # Analyze 10-K data
#             result = analyze_10k(html_content)
#             st.write(result)
#         else:
#             st.warning(f"No 10-K filings found for the symbol {symbol}.")
#     else:
#         st.warning("Please enter a stock symbol.")

    # # Analyze 10-K data
    # if ten_k_text:
    #     analysis_result = analyze_10k(ten_k_text)
    #     display_results(analysis_result)
    # else:
    #     st.warning("Failed to fetch 10-K data. Please check the symbol.")
# else:
#     st.warning("Failed to fetch real-time stock data. Please check the symbol or try again later.")


import yfinance as yf
import requests
import streamlit as st
import plotly.express as px
from datetime import date, timedelta

tabs = ["Prompt","Recommendation", "Company Background", "Investment Thesis", "Catalysts", "Comparable Analysis", "Risk Factors and Mitigating Risk Factors"]
selected_tab = st.sidebar.radio("Select Tab", tabs)


st.title("Stock Pitch Generator")
symbol = st.text_input("Enter a stock symbol: ")
ticker = yf.Ticker(symbol)

if selected_tab == "Recommendation":
    st.header("Recommendation")

if selected_tab == "Company Background":
    st.header("Company Background")
    st.subheader("Past decade chart history:")
    
    start_date = date.today() - timedelta(days=3650)
    end_date = date.today()

    data = yf.download(symbol, start=start_date, end=end_date)
    fig = px.line(data, x=data.index, y=data['Adj Close'], title=symbol)
    st.plotly_chart(fig)

if selected_tab == "Investment Thesis":
    st.header("Investment Thesis")

if selected_tab == "Catalysts":
    st.header("Catalysts")

if selected_tab == "Comparable Analysis":
    st.header("Comparable Analysis")

if selected_tab == "Risk Factors and Mitigating Risk Factors":
    st.header("Risk Factors and Mitigating Risk Factors")
