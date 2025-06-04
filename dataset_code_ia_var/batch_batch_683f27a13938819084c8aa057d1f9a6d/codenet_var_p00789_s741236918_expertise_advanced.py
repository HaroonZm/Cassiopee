from sys import stdin
from functools import lru_cache

N = 18
MAX_SUM = 300

squares = [i * i for i in range(N)]

@lru_cache(maxsize=None)
def count(index, total):
    if total == 0:
        return 1
    if index < 0 or total < 0:
        return 0
    coin = squares[index]
    ways = 0
    for cnt in range(0, total // coin + 1):
        ways += count(index - 1, total - cnt * coin)
    return ways

answers = [count(N - 1, n) for n in range(MAX_SUM + 1)]

for line in stdin:
    n = int(line.strip())
    if n == 0:
        break
    print(answers[n])