import platform, datetime, yfinance as yf

#yfinance documentation: https://pypi.org/project/yfinance/

print('Python version = ' + platform.python_version())
print('yfinance version = ' + yf.__version__)

def yfinancetut(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']
    print('investment: ' + investment)

    today = datetime.datetime.today().isoformat()

    tickerDF = tickerdata.history(period='1d', start='2020-1-1',end=today[:10])
    priceLast = tickerDF['Close'].iloc[-1]
    priceYesterday = tickerDF['Close'].iloc[-2]
    print(tickerDF)

stockDetail = input("Enter Stock Ticker: ")
yfinancetut(stockDetail)
