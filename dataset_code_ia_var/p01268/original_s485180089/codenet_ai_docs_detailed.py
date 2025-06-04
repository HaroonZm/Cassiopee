#! /usr/bin/env python

import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Main(object):
    """
    Main class that encapsulates the methods to solve the given problem.
    """

    def __init__(self):
        """
        Initializes an instance of the Main class.
        """
        pass

    def solve(self):
        """
        Main logic for solving the problem.

        This function repeatedly reads pairs of integers (n, p) from user input.
        For each valid input pair, it finds all primes greater than n,
        generates all possible sums of two (not necessarily distinct) such primes, 
        sorts the resulting list of sums, and prints the p-th smallest sum.
        Ends execution when the input pair (-1, -1) is encountered.
        """
        # Generate a list of prime numbers up to a sufficiently large limit to cover constraints.
        prime = self.sieve(110000)

        while True:
            # Read two integers from input.
            try:
                n, p = map(int, raw_input().split())
            except EOFError:
                break

            # Exit condition
            if n == -1 and p == -1:
                break

            # Filter primes greater than n.
            primes_gt_n = [e for e in prime if e > n]

            # List to hold sums of pairs of primes.
            sums = []

            # Generate all possible sums l[i] + l[j] where i >= j, for first 100 primes greater than n
            for i in range(100):
                for j in range(100):
                    if i < j:
                        continue  # Only consider pairs where i >= j to avoid duplicates
                    sums.append(primes_gt_n[i] + primes_gt_n[j])

            # Sort all generated sums
            sums.sort()

            # Output the p-th smallest sum (1-based index)
            print sums[p-1]

        return None

    def sieve(self, n):
        """
        Finds all prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.

        Args:
            n (int): Upper bound to look for primes (inclusive).

        Returns:
            list: List of all prime numbers up to n.
        """
        # Initialize a boolean array to mark primality of each number
        is_prime = [True for _ in xrange(n + 1)]
        is_prime[0] = False  # 0 is not prime
        is_prime[1] = False  # 1 is not prime

        # Sieve of Eratosthenes main loop
        i = 2
        while i * i <= n:
            if is_prime[i]:
                j = 2
                while i * j <= n:
                    is_prime[i * j] = False
                    j += 1
            i += 1

        # Collect all the primes into a list to return
        return [idx for idx in xrange(n + 1) if is_prime[idx]]


if __name__ == '__main__':
    # Create an instance of Main and invoke solve method.
    m = Main()
    m.solve()