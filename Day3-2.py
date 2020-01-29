import pandas as pd


file = r"F:\WACOMA\PYTHON\data\air.csv"

df= pd.read_csv(file, sep=';' , na_values=[-200])

#print(df.head())

df= pd.read_csv(file, sep=';' , na_values=[-200], parse_dates=[['Date', 'Time']],usecols=['Date','Time' , 'CO(GT)', 'T' , 'RH', 'AH']).rename(columns={'Date_Time' : 'tstamp', 'CO(GT)' : 'CO' , 'T' : 'T', 'RH' :'rel_hum' ,'AH' : 'abs_hum' })
#print(df.head())


#print(df.dtypes)


df['tstamp2'] = pd.to_datetime(df['tstamp'],format='%d/%m/%Y %H.%M.%S')

# print(df.head())
# print(df.dtypes)

df.index = df['tstamp2']
# print(df.index)

# print(df.index.min())
# print(df.index.max())

# print(df.index.day_name())

#print(df.groupby(df.index.day_name())['CO'].mean())

#print(df.groupby(df.index.day_name())['CO'].mean().sort_values(ascending=False))


#print(df.groupby(df.index.hour)['CO'].mean().sort_values(ascending=False))

#print(df.groupby([df.index.day_name(), df.index.hour])['CO'].mean().sort_values(ascending=False))

month_values = df.resample('M') ['CO'].agg(['mean']) # monthly aggregate
print(month_values)

month_values.to_csv(r"F:\WACOMA\PYTHON\data\month_mean.csv")



