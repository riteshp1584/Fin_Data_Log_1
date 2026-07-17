from tradingview_ta import TA_Handler, Interval, Exchange

# Define the parameters for the stock
symbol = "PLATINUM"
exchange = "TVC"

# https://tvdb.brianthe.dev/ (for list of symbols, screeners, exchanges etc.)

# Initialize the TA_Handler
ta_handler = TA_Handler(
    symbol=symbol,
    screener="cfd",  # Use the appropriate screener for your region
    exchange=exchange,
    interval= Interval.INTERVAL_1_DAY  # You can change the interval as needed
)

# Get the analysis
analysis = ta_handler.get_analysis()

# Extract OHLC data
ohlc_data = {
    "open": analysis.indicators['open'],
    "high": analysis.indicators['high'],
    "low": analysis.indicators['low'],
    "close": analysis.indicators['close']
}

print(ohlc_data)
