import yfinance as yf
import requests
import streamlit as st
import plotly.express as px
from datetime import date, timedelta

st.title("Sock Pitch Generator")
symbol = st.text_input("Enter a stock symbol: ")
ticker = yf.Ticker(symbol)

start_date = date.today() - timedelta(days=3650)
end_date = date.today()

data = yf.download(symbol, start=start_date, end=end_date)
fig = px.line(data, x=data.index, y=data['Adj Close'], title=symbol)
st.plotly_chart(fig)

