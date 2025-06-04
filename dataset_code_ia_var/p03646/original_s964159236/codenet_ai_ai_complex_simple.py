from functools import reduce
from operator import add, itemgetter
from itertools import cycle, islice, accumulate, repeat
from collections import deque

k = int(input()) - 1

deck = list(range(49)) + [50]

rot = k % 50
seq = iter(deck)

for _ in range(rot):
    idx = min(enumerate(deck), key=itemgetter(1))[0]
    deck = list(map(lambda x: x[1] + 51 if x[0] == idx else x[1] - 1, enumerate(deck)))

turns = k // 50

deck = list(map(lambda x: x + turns, deck))

print(len(deck))
print(' '.join(map(str, deck)))