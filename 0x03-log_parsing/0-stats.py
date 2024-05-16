#!/usr/bin/python3
""" reads stdin line by line and computes metrics """
import sys


def log_status(dic, size):
    """ logs metrics by printing to stdout """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


status = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            log_status(status, size)

        status_list = line.split()
        count += 1

        try:
            size += int(status_list[-1])
        except:
            pass

        try:
            if status_list[-2] in status:
                status[status_list[-2]] += 1
        except:
            pass
    log_status(status, size)


except KeyboardInterrupt:
    log_status(status, size)
    raise
