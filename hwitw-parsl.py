# Example script for executing HWITW apps on kubernetes

import math
import datetime
import os.path
import netCDF4
import time

import parsl
from parsl import python_app
from parsl.config import Config
from parsl.executors.threads import ThreadPoolExecutor

def main():
    '''Main program to execute all stats calculations by year and latitude.'''
    size = 5

    # Configure parsl to use a local thread pool
    local_threads = Config(
        executors=[ 
            ThreadPoolExecutor( max_threads=10, label='local_threads') 
        ]
    )
    parsl.clear()
    parsl.load(local_threads)

    stat_results = []
    for year in range(size):
        for lat in range(size):
            current_time = datetime.datetime.now()
            print(f'Schedule job at {current_time} for {year} and {lat}')
            stat_results.append(calc_stat_lat(year, lat))
    stats = [r.result() for r in stat_results]
    print(sum(stats))

@python_app
def calc_stat_lat(year, lat):
    current_time = datetime.datetime.now()
    print(f'Starting job at {current_time} for {year} and {lat}')
    prod = year*lat
    time.sleep(5)
    return(prod)


if __name__ == "__main__":
    main()

