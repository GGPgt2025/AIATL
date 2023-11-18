import yfinance as yf

# Function to fetch stock data from Yahoo Finance API
def fetch_stock_data(symbol):
    # Replace 'YOUR_YAHOO_API_KEY' with your actual Yahoo Finance API key
    yahoo_api_key = 'YOUR_YAHOO_API_KEY'
    
    # Construct the API endpoint for real-time stock quotes
    api_url = f'https://finnhub.io/api/v1/quote?symbol={symbol}&token={yahoo_api_key}'

    try:
        response = requests.get(api_url)
        data = response.json()
        return data
    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
        return None
