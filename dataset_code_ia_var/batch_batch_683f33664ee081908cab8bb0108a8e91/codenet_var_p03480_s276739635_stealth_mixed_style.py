import sys
from functools import reduce

sys.setrecursionlimit(10**8)

def get_str():
    return input()

def weird_len(s):
    return len(s)

class Tracker:
    def __init__(self):
        self.ans = 0
        self.prev = 0

def max_func(a, b):
    return a if a > b else b

def iterate(N, func):
    i = 0
    while i < N:
        func(i)
        i += 1

def process(S):
    N = weird_len(S)
    t = Tracker()
    def step(i):
        if S[i] != S[i+1]:
            t.ans = max_func(t.ans, min(N-t.prev, i+1))
            t.prev = i+1
    list(map(step, range(N-1)))
    t.ans = max_func(t.ans, N - t.prev)
    print(t.ans)

if __name__ == "__main__":
    string = get_str()
    process(string)