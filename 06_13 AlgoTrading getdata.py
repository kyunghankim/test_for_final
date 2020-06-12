import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start = datetime.datetime(2016,2,19)
end = datetime.datetime(2019,3,4)
data_test = web.DataReader("AAPL","yahoo",start,end)

plt.plot(data_test.index,data_test['Adj Close'])
plt.show()