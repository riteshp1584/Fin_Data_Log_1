from google.colab import drive
drive.mount('/content/drive')

from IPython.display import Image
Image(filename='/content/drive/MyDrive/Colab Notebooks/Explainer Images/img_1.png')

from IPython.display import Image
Image(filename='/content/drive/MyDrive/Colab Notebooks/Explainer Images/img_2.png')

import yfinance as yf
import pandas as pd

# Define your list of NSE tickers (e.g., RELIANCE.NS, TCS.NS, etc.)
tickers = ["RELIANCE.NS", "TCS.NS",
           "HDFCBANK.NS", "ICICIBANK.NS",
           "CIPLA.NS", "MARUTI.NS",
           "TATASTEEL.NS", "TITAN.NS",
           "BHARTIARTL.NS", "NTPC.NS",
           "ITC.NS", "KOTAKBANK.NS",
           "BAJAJ-AUTO.NS", "SHRIRAMFIN.NS",
           "WIPRO.NS"]

# Fetch data for the last year
data = yf.download(tickers, period="1y")['Close']

momentum_scores = (data.iloc[-1] / data.iloc[0]) - 1
# print(momentum_scores)
ranked_list = momentum_scores.sort_values(ascending=False)
print(ranked_list)

# we use 'qcut' to create 5 bins with labels from Q5 (lowest) to Q1 (highest)
quintiles = pd.qcut(ranked_list, 5, labels=["Q5", "Q4", "Q3", "Q2", "Q1"])

# Display as a Table
df = pd.DataFrame({'Score': ranked_list, 'Quintile': quintiles})
print(df)

# Calculate the spread: (Average of Q1) - (Average of Q5)
spread = df[df['Quintile'] == 'Q1']['Score'].mean() - df[df['Quintile'] == 'Q5']['Score'].mean()

print(f"The Q1-Q5 Momentum Spread is: {spread:.4f}")
