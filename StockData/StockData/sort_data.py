import pandas as pd
from datetime import datetime
df =pd.read_csv('/home/hiep/Desktop/Crawl_Stock_Data/StockData/stock.csv')
arr =[]
for s in df['Ngay']:
    s=datetime.strptime(s,'%d-%m-%Y')
    arr.append(s)
del df['Ngay']
print (arr)
df['Ngay']=arr
df=df.sort_values(by=['Ngay'], ascending=True)
df.to_csv('/home/hiep/Desktop/Crawl_Stock_Data/StockData/StockData/sorted_data.csv')