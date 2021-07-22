import time
import pandas as pd
from website.scripts.sort import read_csv

def min_heap(k):
    start = time.time()
    map = read_csv()
    values = list(map.values())

    # Creating Min Heap for given
    # array with only k elements
    # Create min heap with priority queue
    minHeap = []
    k = int(k)
    for i in range(k):
        minHeap.append(values[i])
     
    # Loop For each element in array
    # after the kth element
    for i in range(k, len(values)):
        minHeap.sort()
         
        # If current element is smaller
        # than minimum ((top element of
        # the minHeap) element, do nothing
        # and continue to next element
        if (minHeap[0] > values[i]):
            continue
             
        # Otherwise Change minimum element
        # (top element of the minHeap) to
        # current element by polling out
        # the top element of the minHeap
        else:
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