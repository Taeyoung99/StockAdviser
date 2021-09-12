#Receive the API from tradingview for stocks
import requests
import json

r = requests.get('https://www.tradingview.com/symbols/NASDAQ-SNDL/')
data = json.loads(r)
print(data)


















#Find the stocks that matches the criteria in basic financial statements(refer to the intelligent
#investor and other sources)












#Use the webscraping to get the relevant news regarding the stocks that u got on previous step.


