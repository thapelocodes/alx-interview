#!/usr/bin/python3
""" Prime Game """
import random


def isWinner(x, nums):
    def sieve(n):
        """
        Returns a list of prime numbers up to n
        (inclusive) using the Sieve of Eratosthenes.
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(n**0.5) + 1):
            if is_prime[start]:
                for multiple in range(start*start, n + 1, start):
                    is_prime[multiple] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    def play_game(n):
        primes = sieve(n)
        if not primes:
            return 'Ben'
        turns = 0  # 0 for Maria's turn, 1 for Ben's turn
        available = [True] * (n + 1)
        while any(available[p] for p in primes):
            available_primes = [p for p in primes if available[p]]
            if not available_primes:
                break
            chosen_prime = random.choice(available_primes)
            for multiple in range(chosen_prime, n + 1, chosen_prime):
                available[multiple] = False
            turns += 1
        return 'Maria' if turns % 2 == 1 else 'Ben'

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
