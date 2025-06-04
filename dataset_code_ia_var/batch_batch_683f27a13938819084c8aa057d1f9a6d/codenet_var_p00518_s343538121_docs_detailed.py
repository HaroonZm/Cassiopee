"""
Schedule Problem Solution
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0595

This script finds the number of valid attendance patterns in a schedule problem,
subject to specific constraints. The problem is solved using dynamic programming
with state representation.
"""

import sys
from collections import Counter
from itertools import product

def solve(n, data):
    """
    Calculates the number of valid attendance patterns for the given schedule.

    Each day is represented by one of 'J', 'O', 'I', standing for which leader
    must be present. The attendance vector for each day ensures the day's leader
    is present, and at least one member from the previous day remains.

    Args:
        n (int): The number of days.
        data (str): A string of length n consisting of 'J', 'O', 'I' per day.

    Returns:
        int: The number of valid attendance patterns modulo 10007.
    """
    # Mapping of each state: attendance of J, O, and I as (j, o, i)
    # Only one possible state on day 0: J is present
    status = Counter({(1, 0, 0): 1})

    # Iterate over each day in the schedule
    for ch in data:
        # Counter to store the possible new states after this day
        u = Counter()
        # Enumerate all possible attendance options (each of J, O, and I can be present or absent)
        for j, o, i in product((0, 1), repeat=3):
            # Proceed only if today's leader is present
            if {'J': j, 'O': o, 'I': i}[ch]:
                # For each previous state, check for at least one overlap with old group
                for k, v in status.items():
                    pj, po, pi = k
                    # Attend today only if at least one member from yesterday's group is present
                    if any([(j and pj), (o and po), (i and pi)]):
                        u[(j, o, i)] += v
        # Apply modulo after each day to keep numbers manageable
        status = Counter({k: v % 10007 for k, v in u.items()})
    # Sum all possible attendance patterns modulo 10007
    return sum(status.values()) % 10007

def main(args):
    """
    Main entry point of the program.

    Reads the number of days and the daily leader schedule from the input,
    computes the number of valid attendance patterns using `solve`, and prints it.

    Args:
        args (list of str): Command-line arguments.
    """
    n = int(input())
    data = input()
    ans = solve(n, data)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])