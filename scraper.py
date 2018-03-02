import pandas as pd
df = pd.read_csv('.txt', index_col = 'date')
df['MA'] = pd.rolling_mean(df.close, window = 60)
df['DayHigh'] = pd.rolling_max(df.high, window = 60)
df['DayLow'] = pd.rolling_min(df.low, window = 60)
print(df.head())
print(type(df))
print(df.index)
print(df.columns)
# df = df.ix[0:2, :]
# df = df.ix[:, ['close']]
# df = df.ix[0, ['close']]
print(df.head())
import matplotlib.pyplot as plt
df.plot()
# df['close'].plot()
# df['close'].plot(title = '2330', figsize = (15, 10))
df[['close', 'MA', 'DayHigh', 'DayLow']].plot(title = '2330', figsize = (20, 15))
plt.show()
