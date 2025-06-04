from functools import partial
from collections import deque
import sys

def solve():
    input = sys.stdin.readline
    buffer_size = 100003
    a = [0] * buffer_size

    while True:
        try:
            n_k = input()
            if not n_k:
                break
            n, k = map(int, n_k.split())
            if n == 0:
                break
            dq = deque()
            max_sum = curr_sum = 0
            for i in range(n):
                a[i] = int(input())
            curr_sum = sum(a[:k])
            max_sum = curr_sum
            for i in range(k, n):
                curr_sum += a[i] - a[i - k]
                if curr_sum > max_sum:
                    max_sum = curr_sum
            print(max_sum)
        except EOFError:
            break

solve()