import yfinance as yf
import pandas as pd

apple = yf.Ticker("AAPL")
#!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json

import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable   
    #print("Type:", type(apple_info))
apple_info
apple_info['country']

# Extracting Share Price
apple_share_price_data = apple.history(period="max")
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")

# Extracting Dividends
apple.dividends
apple.dividends.plot()