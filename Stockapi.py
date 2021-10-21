import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'ICUTXZ1NUQTWDMNJ'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
print(data)

#make a loop function that runs through the list of s&p 500 stocks into symbol parameter

sp500 = ["AAPL", "MSFT", "AMZN", "GOOGL", "FB", "GOOG", "TSLA","NVDA", "BRK.B", "JPM"
         "JNJ", "UNH", "V", "HD", "BAC", "PG", "PYPL", "MA", "DIS", "ADBE"
         "CRM", "NFLX", "XOM", "CMCSA", "PFE", "CSCO", "TMO", "INTC", "ACN", "PEP",
         "VZ", "CVX", "ABT", "KO", "AVGO", "WMT", "WFC", "COST", "NKE", "MRK",
         ""]































#Make gui to show the data visually.(There are softwares for it)


