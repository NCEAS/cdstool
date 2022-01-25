# Example script for executing HWITW apps on kubernetes

import math
import datetime
import os.path
import time

import parsl
from parsl import python_app

def main():
    '''Main program to execute all stats.'''

    #from parslexec import local_exec
    #from parslexec import htex_local
    from parslexec import htex_kube
    parsl.load(htex_kube)

    size = 5
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

