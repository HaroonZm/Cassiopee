from sys import stdin
from collections import deque

def solve():
    N, M, Q = map(int, stdin.readline().split())
    student = deque(range(N))
    exemption = [1] * N

    for a in map(int, stdin.readline().split()):
        student.rotate(a if a & 1 else -a)
        exemption[student.popleft()] = 0

    answers = (exemption[q] for q in map(int, stdin.readline().split()))
    print(*answers, sep='\n')

solve()