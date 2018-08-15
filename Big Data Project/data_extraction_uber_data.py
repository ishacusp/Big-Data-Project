import os

try:
    from sodapy import Socrata as sc
except:
    os.system(pip install sodapy)

import pandas as pd
import datetime as dt
import credentials as cd

def main():
    client = sc(domain = "data.cityofnewyork.us", app_token = cd.app_token, username = cd.username, password = cd.password)

    results = client.get("edp9-qgv4", limit=1000)

    data = pd.DataFrame.from_records(results)
    data_short = data[['base_license_number','base_name','dba']]

    data_apr14 = pd.read_csv('uber-raw-data-apr14.csv')
    data_aug14 = pd.read_csv('uber-raw-data-aug14.csv')
    data_may14 = pd.read_csv('uber-raw-data-may14.csv')
    data_jun14 = pd.read_csv('uber-raw-data-jun14.csv')
    data_jul14 = pd.read_csv('uber-raw-data-jul14.csv')
    data_sep14 = pd.read_csv('uber-raw-data-sep14.csv')

    data_14 = pd.concat([data_apr14, data_may14, data_jun14, data_jul14, data_aug14, data_sep14], axis=0)

    data_14 = data_14.merge(data_short, left_on = 'Base', right_on = 'base_license_number', how='inner')

    data_14['datetime'] = [dt.datetime.strptime(i, '%m/%d/%Y %H:%M:%S') for i in data_14['Date/Time']]

    data_14.to_csv('uber_pickups_apr-sep_14.txt')



if __name__ == "__main__":
    main()
