from collections import Counter
from functools import reduce
import sys

S = sys.stdin.readline().strip()

def count_removal(s):
    counter = 0
    for c in s:
        counter += 1 if c == 'S' else -1
        counter = max(counter, 0)
    return counter + s.count('T') - (len(s) - counter - s.count('T'))

print(count_removal(S))