import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = 'ICUTXZ1NUQTWDMNJ'

ts = TimeSeries(key=api_key, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval = '1min', outputsize = 'full')
print(data)

#make a loop function that runs through the list of top change in percentage stocks that day and evaluate if it has potential
#Use technical analysis

topgainer = ["DWACU", "DWAC", "SGAMU", "TSC", "EAR"]


         































#Make gui to show the data visually.(There are softwares for it)


