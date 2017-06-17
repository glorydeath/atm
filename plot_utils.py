import datetime
import matplotlib.finance as finance
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
import moving_average as ma
import matplotlib.ticker as mticker


def plot(r, ma3, ma13, ma34):
    print 'ploting in plot utils'
    plt.rc('axes', grid=True)
    plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)

    # textsize = 9
    # left, width = 0.1, 0.8
    # rect = [left, 1.1, width, 0.8]
    # fig = plt.figure(facecolor='white')
    # axescolor = '#f6f6f6'
    #
    # prices = r.adj_close
    # dx = r.adj_close - r.close
    # low = r.low + dx
    # high = r.high + dx
    #
    # deltas = np.zeros_like(prices)
    # deltas[1:] = np.diff(prices)
    # up = deltas > 0
    #
    # ax1 = fig.add_axes(rect, axisbg=axescolor)
    # ax1.vlines(r.date[up], low[up], high[up], color='black', label='_nolegend_')
    # ax1.vlines(r.date[~up], low[~up], high[~up], color='black', label='_nolegend_')

    linema3, = plt.plot(r.date, ma3, color='blue', lw=1, label='EMA (3)')
    linema3, = plt.plot(r.date, ma13, color='green', lw=1, label='EMA (13)')
    linema3, = plt.plot(r.date, ma34, color='red', lw=1, label='EMA (34)')
    # linema3, = ax1.plot(r.date, ma3, color='blue', lw=1, label='EMA (3)')
    # linema13, = ax1.plot(r.date, ma13, color='green', lw=1, label='EMA (13)')
    # linema34, = ax1.plot(r.date, ma34, color='red', lw=1, label='EMA (34)')
    # ax1.yaxis.set_major_locator(mticker.MaxNLocator(5, prune='both'))
    plt.show()


print 'Plot utils'

startdate = datetime.date(2016, 1, 1)
today = enddate = datetime.date.today()
ticker = 'AMZN'

fh = finance.fetch_historical_yahoo(ticker, startdate, enddate)
# a numpy record array with fields: date, open, high, low, close, volume, adj_close)

r = mlab.csv2rec(fh)
fh.close()
r.sort()

print 'Plot utils. Sorted'

ma3 = ma.moving_average(3, startdate)
ma13 = ma.moving_average(13, startdate)
ma34 = ma.moving_average(34, startdate)
plot(r, ma3, ma13, ma34)

print 'plot utils done'
