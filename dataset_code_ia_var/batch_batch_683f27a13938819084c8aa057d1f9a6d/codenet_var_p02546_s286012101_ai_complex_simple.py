import sys
from functools import reduce
from operator import add

input_ = sys.stdin.readline
S = input_().strip()

def next_plural(word):
    return reduce(add, [word, 'es'*(word.endswith('s')) or 's'])

print(next_plural(S))