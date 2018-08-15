import pandas as pd
import os
import glob
from datetime import datetime

dfs = []
for path in glob.glob('/Users/ishachaturvedi/Isha/BigData/HW8/2014/*.csv'):
    try:
        df = pd.read_csv(path, skiprows=1)
        date_str = os.path.splitext(os.path.basename(path))[0]
        date = datetime.strptime(date_str, '%Y%m%d')
        df['date'] = date
        dfs.append(df)
    except Exception as e:
        print('error:', path, 'not loaded.', e)
df = pd.concat(dfs)
df.head()


df.to_csv("2014.csv",index =  True)