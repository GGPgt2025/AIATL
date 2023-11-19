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

