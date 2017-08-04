import datetime
import matplotlib.finance as finance
import numpy as np
import matplotlib.mlab as mlab

today = datetime.date.today()
startdate = today - datetime.timedelta(days=90)
yesterday = today - datetime.timedelta(days=1)
ticker = 'AMZN'


def moving_average(n, startdate, enddate=today, t=ticker, type='exponential'):
    """
    return the moving average for a specific startdate, enddate and ticker
    :param n:
    :param startdate:
    :param enddate:
    :param t:
    :param type:
    :return: moving average as a numpy.ndarray
    """
    fh = finance.fetch_historical_yahoo(t, startdate, enddate)
    r = mlab.csv2rec(fh)
    fh.close()
    r.sort()
    prices = r.adj_close

    x = np.asarray(prices)
    if type == 'simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))

    weights /= weights.sum()

    a = np.convolve(x, weights, mode='full')[:len(x)]
    a[:n] = a[n]
    return a

ma3 = moving_average(3, startdate)
ma13 = moving_average(13, startdate)
ma34 = moving_average(34, startdate)

print ma3
print ma13
print ma34