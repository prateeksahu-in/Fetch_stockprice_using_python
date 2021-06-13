import time
import datetime
import pandas as pd

company = 'RELIANCE.NS'  # you can change the name with desired company
period1 = int(time.mktime(datetime.datetime(2020, 12, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))
interval = '1d'  # 1d, 1m

yahoo_query = f'https://query1.finance.yahoo.com/v7/finance/download/{company}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true '

df = pd.read_csv(yahoo_query)
# print(df)
df.to_csv('stock_price_data.csv')
# after downloading if the date is coming as ###### in some col you can try converting it from "Genral" to "Date
# Short" from number option in MS excel
