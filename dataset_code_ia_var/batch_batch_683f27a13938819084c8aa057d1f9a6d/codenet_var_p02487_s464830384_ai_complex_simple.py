import sys
import math
import functools
import itertools
import operator

def solve():
    # Custom input function to be compatible with both Python 2 and 3
    try:
        _input = raw_input
    except NameError:
        _input = input

    # Lambda to build a line with function composition and slicing
    border = lambda n: ''.join(itertools.repeat('#', n))
    fill = lambda n: '#' + ''.join(itertools.repeat('.', n - 2)) + '#' if n > 1 else '#'
    fancy_rect = lambda a, b: list(itertools.chain(
        [border(b)],
        (fill(b) for _ in range(a - 2)),
        [border(b)] if a > 1 else []
    ))

    # Infinite loop using iter with a sentinel
    for ab in iter(lambda: list(map(int, _input().split())), [0,0]):
        a, b = ab
        # Use map with print to output lines
        list(map(lambda line: sys.stdout.write(line + '\n'), fancy_rect(a, b)))
        sys.stdout.write('\n')

if __name__ == "__main__":
    solve()