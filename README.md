# AIATL
The Stock Pitch Generator is a Python-based application that allows users to generate a stock pitch from the most recent annual company filing (10-K report) for any stock listed in the S&P500.

## Features

- Select any stock from the S&P500 to analyze.
- Fetches real-time stock data using the Yahoo Finance API.
- Analyzes the most recent annual company filing (10-K) for the selected stock.
- Generates a stock pitch deck based on the analysis.

## Project Structure

The project is organized into the following directories:

- **`app/`**: Contains the Streamlit app code and user interface logic.
- **`analysis/`**: Holds code related to the analysis of 10-K reports.
- **`api/`**: Contains code for fetching real-time stock data from external APIs.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/GGPgt2025/AIATL.git
    ```

2. Navigate to the project directory:

    ```bash
    cd stock-pitch-generator
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app/main_app.py
    ```

5. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the Stock Pitch Generator.

6. Enter the stock symbol (e.g., AAPL) in the input field and follow the on-screen instructions to generate a stock pitch.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Other dependencies...]

## Disclaimer

This project is for educational and informational purposes only. The accuracy of the stock analysis and pitch generated by the application is not guaranteed. Make your investment decisions based on thorough research and consultation with financial professionals.

## License

This project is licensed under the (LICENSE).