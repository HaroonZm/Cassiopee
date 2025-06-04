from functools import reduce
from operator import sub
from itertools import accumulate, islice

A,B,K = map(int,input().split())

def fancy_logic(A,B,K):
    cases = [
        lambda : (reduce(sub, (A,K)), B),
        lambda : (0, list(islice(accumulate([-K, A, B]),2))[-1]),
        lambda : (0,0)
    ]
    idx = min(reduce(lambda x, y: x + (K > y), [A, A+B]), 2)
    return cases[idx]()

print(*fancy_logic(A,B,K))