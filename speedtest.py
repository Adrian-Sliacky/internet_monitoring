import speedtest
import csv
import time
import datetime
from os import path
import os

path_to_file = 'speedtest_data.csv'
file_header = ['timestamp','download', 'upload', 'ping']

try:
    f_size = os.path.getsize(path_to_file)
except FileNotFoundError as e:
    pass

make_csv_header = False
if not path.exists(path_to_file) or f_size == 0:
    make_csv_header = True

with open(path_to_file, 'a') as file:
    writer = csv.writer(file)
    if make_csv_header:
        writer.writerow(file_header)
def test():
    """
    take about 32 - 37 seconds (down and up)
    makes speedtest - returns download, upload and ping to the server
    """
    s = speedtest.Speedtest()
    # s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    result = s.results.dict()
    return result["download"], result["upload"], result["ping"]

def speed_tst():
    d, u, p = test()
    res = []
    res.append([str(datetime.datetime.now()),str(d/(10**6)), str(u/(10**6)), str(p)]) # devided by 10^6 for conversion from bits/s to mbits
    return res
    

def write_list(data_to_write):
    with open(path_to_file, 'a') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_write)

def speedtest_core():
    write_list(speed_tst())
    
while True:
    speedtest_core()
    time.sleep(60) # make speedtest every x secs
