import time
import datetime
from pythonping import ping
import csv
import os
from os import path

path_to_file = 'ping_times.csv'
servers = [
  "apple.com",
  "github.com",
  "google.com",
  "1.1.1.1",
  "discord.com",
  "speedtest.detronics.sk"
  ]

file_header = ['time', 'server', 'latency']

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


def write_list(data_to_write):
    with open('ping_times.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_write)



def avg_ping(site, times=2):
    return round(ping(site, verbose=False, count=times).rtt_avg*1000, 3) # times 1000 to convert to ms

def ping_all_servers():
    network_data_to_write = []
    for _ in servers:
        p = avg_ping(_)
        network_data_to_write.append([str(datetime.datetime.now()), str(_), str(p)])
    return (network_data_to_write)

def ping_core():
    write_list(ping_all_servers())


while True:
    ping_core()
    time.sleep(10) # send these pings every x seconds
