from functools import reduce
from itertools import islice, chain, repeat, permutations
from collections import deque, defaultdict
from heapq import *
from operator import itemgetter

MOVE = ((1, 4), (0, 2, 5), (1, 3, 6), (2, 7), (0, 5), (1, 4, 6), (2, 5, 7), (3, 6))
GOAL = "01234567"
answers = defaultdict(lambda: float("inf"))
answers[GOAL] = 0

swap = lambda s, i, j: ''.join(list(map(lambda kv: kv[1], sorted(enumerate(list(s)), key=lambda x: (j if x[0]==i else (i if x[0]==j else x[0]))))))

def bfs_palindrome():
    explore = deque([(0, GOAL)])
    while explore:
        cost, puzzle = explore.popleft()
        idx = puzzle.index('0')
        transform = lambda i: swap(puzzle, idx, i)
        layers = list(map(transform, MOVE[idx]))
        for neighbor in layers:
            if answers[neighbor] > cost+1:
                answers[neighbor]=cost+1
                explore.append((cost+1, neighbor))
bfs_palindrome()

for request in iter(lambda: __import__('sys').stdin.readline().replace(' ', '').strip(), ""):
    print(answers[request])