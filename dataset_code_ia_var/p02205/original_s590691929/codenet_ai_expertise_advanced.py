from itertools import islice, accumulate
from operator import add

N = int(input())
A, B = map(int, input().split())

def transitions(A, B):
    yield A, B
    for i in range(1, 12):
        if i % 2:
            A -= B
        else:
            B += A
        yield A, B

print(*next(islice(transitions(A, B), N % 12, None)))