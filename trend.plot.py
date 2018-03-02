import pandas as pd
import matplotlib.pyplot as plt
import datetime
# import tradingWithPython
# from tradingWithPython import yahooFinance as yf

start = datetime.date(2016, 1, 1)
end = datetime.date(2017, 1 , 1)
# end = datetime.date.today
dates = pd.date_range(start, end)
print(dates)
df_temp = pd.DataFrame(index = dates)
print(df_temp)
symbols = ['2330', '2317', '1301', '1303']

for symbol in symbols:
    path = 'C:/Users/User/Python_Capital_20180131/output/' + symbol + '.txt'
    df = pd.read_csv(path, index_col = 'date')
    df = df.ix[:, ['close']]
    df = df.rename(columns = {'close':symbol})
    df_temp = df_temp.join(df).dropna()

df_temp = df_temp/df_temp.ix[0,:]    
w = [0.25, 0.25, 0.25, 0.25]
equal_w = df_temp*w
equal_w['sum'] = equal_w.sum(axis = 1)
equal_w['daily_R'] = equal_w['sum']/equal_w['sum'].shift(1) - 1
sharp = equal_w['daily_R'].mean()/equal_w['daily_R'].std()*(252**0.5)
equal_w['rolling_mean'] = pd.rolling_mean(equal_w['daily_R'], window = 60)
equal_w['rolling_std'] = pd.rolling_std(equal_w['daily_R'], window = 60)
equal_w['rolling_sharp'] = equal_w['rolling_mean']/equal_w['rolling_std']

print('equal_w/n', equal_w.head())
print('sharp', sharp)
print(equal_w.head())
print(df_temp.head())
df_temp.plot()
equal_w['sum'].plot()
equal_w['rolling_sharp'].plot(figsize = (20, 15))
plt.show()

# df = pd.read_csv('C:/Users/User/Python_Capital_20180131/output/2330.txt', index_col = 'date')
# df['MA'] = pd.rolling_mean(df.close, window = 60)
# df['DayHigh'] = pd.rolling_max(df.high, window = 60)
# df['DayLow'] = pd.rolling_min(df.low, window = 60)
# print(df.head())
# print(type(df))
# print(df.index)
#print(df.columns)
# df = df.ix[0:2, :]
# df = df.ix[:, ['close']]
# df = df.ix[0, ['close']]
# print(df.head())
# import matplotlib.pyplot as plt
# df.plot()
# df['close'].plot()
# df['close'].plot(title = '2330', figsize = (15, 10))
# df[['close', 'MA', 'DayHigh', 'DayLow']].plot(title = '2330', figsize = (20, 15))
# plt.show()
