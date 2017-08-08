from IPython import get_ipython
from googlefinance import getQuotes
from yahoo_finance import Share
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import datetime
import json
import csv


#apple = Share('AAPL')
#print(apple.get_open())
#print(apple.get_price())
#print(apple.get_trade_datetime())

start = datetime.datetime(2016,1,1)
end = datetime.datetime(2016, 8, 1)

stocks = []
with open('companyList.csv') as csvfile:
    stockreader = csv.reader(csvfile)
    for row in stockreader:
        print(str(row)[2:][:-2].upper())
        x = Share(str(row)[2:][:-2].upper())
        print(x.get_price())
        #stocks.append(str(row)[2:][:-2].upper())

#for stock in stocks:
#    q = web.get_quote_google(stock)
#    print(q)

#amazon = web.DataReader("AAPL", "yahoo", start, end)
#close = amazon["Close"]
#close.plot()
#print(type(amazon))
#print(amazon)
#pylab.rcParams['figure.figsize'] = (15,9)

#plt.show()

#print(amazon.ix['2016-02-04'])

#q = web.get_quote_google(['AMZN', 'GOOG'])
#print(q)

#print(json.dumps(getQuotes('AAPL'), indent=2))
#[
#    {
#        "Index": "NASDAQ",
#        "LastTradeWithCurrency": "129.09",
#    }
#]
