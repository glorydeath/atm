import datetime
import numpy as np
import matplotlib.finance as finance
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

startdate = datetime.date(2016, 1, 1)
today = enddate = datetime.date.today()
ticker = 'AAPL'

fh = finance.fetch_historical_yahoo(ticker, startdate, enddate)
# a numpy record array with fields: date, open, high, low, close, volume, adj_close)

# now it's sorted from now to previous
r = mlab.csv2rec(fh)
fh.close()
r.sort()

prices = r.adj_close

dx = r.adj_close - r.close
low = r.low + dx
high = r.high + dx

deltas = np.zeros_like(prices)
deltas[1:] = np.diff(prices)

print deltas
up = deltas > 0
print up
print r.date[~up]
print r.date[up]