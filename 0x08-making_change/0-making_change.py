#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ Finds the least number of coins that add up to a given sum. """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    temp = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            temp += 1
        if total == 0:
            return temp
    
    return -1