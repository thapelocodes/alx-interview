#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """ Generate changes required to reach total.

    Args:
        coins (list): List of coin denominations available.
        total (int): Total amount needed.
        
    Returns:
        int: Minimum number of coins needed to make the total, or -1 if not possible.
    """
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    counter = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            counter += 1
        if total == 0:
            return counter
    
    return -1