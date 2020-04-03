import pandas as pd
import datetime
import pandas_datareader.data as web
import math
import pandas as pd
import numpy as np
import preprocessing

from pandas import Series, DataFrame
import yfinance as yf

company = "GE"

df = yf.download(company, start = '2016-01-01', end='2020-03-28')

close_px = df['Adj Close']
mavg = close_px.rolling(window=100).mean()

print(mavg)

print(df.head())

print(df.tail())

import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label=company)
mavg.plot(label='mavg')
plt.legend()

plt.show()

rets = close_px / close_px.shift(1) - 1
rets.plot(label='return')

plt.show()


dfcomp = yf.download(['AAPL', 'GE', 'GOOG', 'IBM', 'MSFT'],start = '2016-01-01', end='2020-03-28')['Adj Close']

print(dfcomp.tail())


retscomp = dfcomp.pct_change()

corr = retscomp.corr()

# print(corr)

# plt.scatter(retscomp.AAPL, retscomp.GE)
# plt.xlabel('Returns-AAPL')
# plt.ylabel('Returns-GE')

# plt.show()


#   Error
#pd.scatter_matrix(retscomp, diagonal='kde', figsize=(10, 10));



plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)

plt.show()


# plt.scatter(retscomp.mean(), retscomp.std())
# plt.xlabel('Expected returns')
# plt.ylabel('Risk')
# for label, x, y in zip(retscomp.columns, retscomp.mean(), retscomp.std()):
#     plt.annotate(
#         label, 
#         xy = (x, y), xytext = (20, -20),
#         textcoords = 'offset points', ha = 'right', va = 'bottom',
#         bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
#         arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

# plt.show()

dfreg = df.loc[:,['Adj Close','Volume']]

a=df['High'] - df['Close']
print(a)


dfreg['HL_PCT'] = a / df['Close'] * 100.0
print("yo --- yo ")

print(dfreg['HL_PCT'])

print(df['Close'])
print(df['Open'])

b = df['Close'] - df['Open']

dfreg['PCT_change'] = b / df['Open'] * 100.0

# import math
# import numpy as np
# from sklearn import preprocessing, svm
# from sklearn.model_selection import train_test_split


# # Drop missing value
# dfreg.fillna(value=-99999, inplace=True)

# print(dfreg.shape)
# # We want to separate 1 percent of the data to forecast
# forecast_out = int(math.ceil(0.01 * len(dfreg)))

# # Separating the label here, we want to predict the AdjClose
# forecast_col = 'Adj Close'
# dfreg['label'] = dfreg[forecast_col].shift(-forecast_out)
# X = np.array(dfreg.drop(['label'], 1))

# # Scale the X so that everyone can have the same distribution for linear regression
# X = preprocessing.scale(X)

# # Finally We want to find Data Series of late X and early X (train) for model generation and evaluation
# X_lately = X[-forecast_out:]
# X = X[:-forecast_out]

# # Separate label and identify it as y
# y = np.array(dfreg['label'])
# y = y[:-forecast_out]

# print('Dimension of X',X.shape)
# print('Dimension of y',y.shape)

# # Separation of training and testing of model by cross validation train test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# from sklearn.linear_model import LinearRegression
# from sklearn.neighbors import KNeighborsRegressor

# from sklearn.linear_model import Ridge
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.pipeline import make_pipeline

# # Linear regression
# clfreg = LinearRegression(n_jobs=-1)
# clfreg.fit(X_train, y_train)


# # Quadratic Regression 2
# clfpoly2 = make_pipeline(PolynomialFeatures(2), Ridge())
# clfpoly2.fit(X_train, y_train)

# # Quadratic Regression 3
# clfpoly3 = make_pipeline(PolynomialFeatures(3), Ridge())
# clfpoly3.fit(X_train, y_train)
    
# # KNN Regression
# clfknn = KNeighborsRegressor(n_neighbors=2)
# clfknn.fit(X_train, y_train)

# confidencereg = clfreg.score(X_test, y_test)
# confidencepoly2 = clfpoly2.score(X_test,y_test)
# confidencepoly3 = clfpoly3.score(X_test,y_test)
# confidenceknn = clfknn.score(X_test, y_test)

# print("The linear regression confidence is ",confidencereg)
# print("The quadratic regression 2 confidence is ",confidencepoly2)
# print("The quadratic regression 3 confidence is ",confidencepoly3)
# print("The knn regression confidence is ",confidenceknn)

# # Printing the forecast
# forecast_set = clfreg.predict(X_lately)
# dfreg['Forecast'] = np.nan
# print(forecast_set, confidencereg, forecast_out)


# last_date = dfreg.iloc[-1].name
# last_unix = last_date
# next_unix = last_unix + datetime.timedelta(days=1)

# for i in forecast_set:
#     next_date = next_unix
#     next_unix += datetime.timedelta(days=1)
#     dfreg.loc[next_date] = [np.nan for _ in range(len(dfreg.columns)-1)]+[i]


    
# dfreg['Adj Close'].tail(500).plot()
# dfreg['Forecast'].tail(500).plot()
# plt.legend(loc=4)
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.show()


from scipy.stats import norm

# data = yf.download("AAPL", start = '2012-01-01', end='2017-01-01')['Adj Close']


result=[]
#Define Variables
S = yf.download(company, start = '2016-01-01', end='2020-03-28')['Adj Close'][-1]#apple['Adj Close'][-1] #starting stock price (i.e. last available real stock price)
T = 50 #Number of trading days
days = (df.index[-1] - df.index[0]).days
cagr = ((((df['Adj Close'][-1]) / df['Adj Close'][1])) ** (365.0/days)) - 1
mu = cagr# 0.2309 #Return

df['Returns'] = df['Adj Close'].pct_change()
vol = df['Returns'].std()*math.sqrt(252)
# vol = #0.4259 #Volatility


#choose number of runs to simulate - I have chosen 10,000
for i in range(100):
    #create list of daily returns using random normal distribution
    daily_returns=np.random.normal(mu/T,vol/math.sqrt(T),T)+1
    
    #set starting price and create price series generated by above random daily returns
    price_list = [S]
    
    for x in daily_returns:
        price_list.append(price_list[-1]*x)

    #plot data from each individual run which we will plot at the end
    plt.plot(price_list)
    
    #append the ending value of each simulated run to the empty list we created at the beginning
    result.append(price_list[-1])

#show the plot of multiple price series created above
plt.show()

#create histogram of ending stock values for our mutliple simulations
plt.hist(result,bins=50)
plt.show()


#use numpy mean function to calculate the mean of the result
print(round(np.mean(result),2))



# t_intervals = 30 # time steps forecasted into future
# iterations = 25 # amount of simulations

# log_returns = np.log(1 + data.pct_change())

# log_returns.plot(figsize = (10, 6))

# #Setting up drift and random component in relation to asset data
# u = log_returns.mean()
# var = log_returns.var()
# drift = u - (0.5 * var)
# stdev = log_returns.std()
# daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
# #Takes last data point as startpoint point for simulation
# S0 = data.iloc[-1]
# price_list = np.zeros_like(daily_returns)
# price_list[0] = S0
# #Applies Monte Carlo simulation in asset
# for t in range(1, t_intervals):
#     price_list[t] = price_list[t - 1] * daily_returns[t]

# plt.figure(figsize=(10,6))
# plt.plot(price_list)



# data = yf.download("AAPL", start = '2012-01-01', end='2017-01-01')['Adj Close']

# t_intervals = 30 # time steps forecasted into future
# iterations = 25 # amount of simulations

# log_returns = np.log(1 + data.pct_change())

# log_returns.plot(figsize = (10, 6))

# #Setting up drift and random component in relation to asset data
# u = log_returns.mean()
# var = log_returns.var()
# drift = u - (0.5 * var)
# stdev = log_returns.std()
# daily_returns = np.exp(drift.values + stdev.values * norm.ppf(np.random.rand(t_intervals, iterations)))
# #Takes last data point as startpoint point for simulation
# S0 = data.iloc[-1]
# price_list = np.zeros_like(daily_returns)
# price_list[0] = S0
# #Applies Monte Carlo simulation in asset
# for t in range(1, t_intervals):
#     price_list[t] = price_list[t - 1] * daily_returns[t]

# plt.figure(figsize=(10,6))
# plt.plot(price_list)