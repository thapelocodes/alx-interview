#!/usr/bin/python3
"""
solves the log parsing problem
"""
import sys


def log_status(dic, size):
    """ function to print logs """
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
            log_status(sts, size)

        status_li = line.split()
        count += 1

        try:
            size += int(status_li[-1])
        except:
            pass

        try:
            if status_li[-2] in status:
                status[status_li[-2]] += 1
        except:
            pass
    log_status(status, size)


except KeyboardInterrupt:
    log_status(status, size)
    raise
