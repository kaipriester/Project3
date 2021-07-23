import time
from website.scripts.sort import read_csv

def min_heap(k):
    start = time.time()
    map = read_csv()
    values = list(map.values())

    minHeap = []
    k = int(k)
    for i in range(k):
        minHeap.append(values[i])

    for i in range(k, len(values)):
        #minHeap.sort()
        if (not minHeap[0] > values[i]):
            minHeap.pop(0)
            minHeap.append(values[i])
            
    date_time = []
    wind_speeds = []

    for i in minHeap:
        wind_speeds.append(i)
        #print(i, end=' ')
        date_time.append(list(map.keys())[list(map.values()).index(i)])
        #print(list(map.keys())[list(map.values()).index(i)], end=' ')
    
    end = time.time()
    timer = end - start
    
    return date_time, wind_speeds, timer