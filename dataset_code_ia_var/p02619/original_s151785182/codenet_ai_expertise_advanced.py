import sys
import numpy as np
from functools import reduce
from typing import List, Final

class Game:
    __slots__ = 'c', 's'

    def __init__(self, c: List[int], s: List[List[int]]):
        self.c = np.array(c, dtype=int)
        self.s = np.array(s, dtype=int)

def solve(D: int, c: List[int], s: List[List[int]], t: List[int]) -> List[int]:
    c_np: Final = np.array(c, dtype=int)
    s_np: Final = np.array(s, dtype=int)
    last = np.zeros(26, dtype=int)
    score = 0
    total_c = c_np.sum()
    results = []
    for day, contest in enumerate(t, 1):
        idx = contest - 1
        score += s_np[day-1, idx]
        last += 1
        last[idx] = 0
        score -= np.dot(last, c_np)
        results.append(score)
    return results

def main():
    input_iter = (word for line in sys.stdin for word in line.split())
    D = int(next(input_iter))
    c = [int(next(input_iter)) for _ in range(26)]
    s = [[int(next(input_iter)) for _ in range(26)] for _ in range(D)]
    t = [int(next(input_iter)) for _ in range(D)]
    print(*solve(D, c, s, t), sep="\n")

if __name__ == "__main__":
    main()