#!/usr/bin/python3
"""
Method that determines the number of minmum operations given n characters
"""


def minOperations(n):
    """
        calculates the fewest number of operations needed to give a
        result of exactly n H characters in a file args: n: Number
        of characters to be displayed
    """
    now = 1
    start = 0
    cntr = 0
    while now < n:
        rem = n - now
        if (rem % now == 0):
            start = now
            now += start
            cntr += 2
        else:
            now += start
            cntr += 1
    return cntr
