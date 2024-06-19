#!/usr/bin/python3
''' Making Change '''


def makeChange(coins, total):
    ''' Finds the least number of coins that add up to a given sum. '''
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    counter = 0
    
    for coin in coins:
        while(total >= coin):
            total -= coin
            counter += 1

    if total == 0:
        return counter
    total += coin
    counter -= 1
    
    return -1
