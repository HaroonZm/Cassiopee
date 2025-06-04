from functools import reduce
from operator import eq

def bubble_sort(A, N):
    swap_count = [0]
    flag = [True]
    idx = [0]
    def inner(flag, idx, A, swap_count):
        return (lambda _: swap_count[0] if not flag[0] else _
            )((lambda:(
            flag.__setitem__(0, False),
            list(map(
                lambda j: (
                    (lambda cond: (
                        (A.__setitem__(j-1, A[j-1]^A[j]), A.__setitem__(j, A[j-1]^A[j]), 
                        A.__setitem__(j-1, A[j-1]^A[j]), swap_count.__setitem__(0, swap_count[0]+1), flag.__setitem__(0,True)
                        ) if cond else None
                    ))(A[j] < A[j-1])
                ),
                range(N-1, idx[0], -1)
            )),
            idx.__setitem__(0, idx[0]+1),
            inner(flag, idx, A, swap_count)
        )[3])())
    return inner(flag, idx, A, swap_count)

from itertools import count, takewhile, starmap

def readN():
    return int(__import__('sys').stdin.readline())

def readA(N):
    return list(starmap(int, zip([__import__('sys').stdin.readline()]*N, (range(N)))))

for N in iter(readN, 0):
    A = [int(__import__('sys').stdin.readline()) for _ in range(N)]
    print(bubble_sort(A, N))