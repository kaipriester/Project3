#import csv
import time
import pandas as pd

def read_csv():
    file = "website/data/wmo_41010_5d09_dfd3_3935.csv"

    map = pd.read_csv(file, index_col=0, squeeze=True, skiprows=0).dropna().to_dict()

    return map   

def sort_array(k):
    start = time.time()
    map = read_csv()
    values = list(map.values())
    values.sort(reverse = True)

    date_time = []
    wind_speeds = []

    for i in range(int(k)):
        wind_speeds.append(values[i])
        #print(wind_speeds.append(values[i]))
        date_time.append(list(map.keys())[list(map.values()).index(values[i])])
        #print(date_time.append(list(map.keys())[list(map.values()).index(values[i])]))
    
    end = time.time()
    timer = end - start

    return date_time, wind_speeds, timer