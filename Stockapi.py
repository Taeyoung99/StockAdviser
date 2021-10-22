import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'ICUTXZ1NUQTWDMNJ'
topgainer = ["DWACU", "DWAC", "SGAMU", "TSC", "EAR"]



ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol="DWACU", outputsize = 'full')
print(data)

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol="DWAC", outputsize = 'full')
print(data)

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol="SGAMU", outputsize = 'full')
print(data)

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol="TSC", outputsize = 'full')
print(data)

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_daily(symbol="EAR", outputsize = 'full')
print(data)


#make a loop function that runs through the list of top change in percentage stocks that day and evaluate if it has potential
#Use technical analysis



         































#Make gui to show the data visually.(There are softwares for it)


