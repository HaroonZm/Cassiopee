from sys import stdin

def solve():
    A, B, C = map(int, stdin.readline().split())
    if C % gcd(A, B) != 0:
        print('NO')
        return
    visited = set()
    rem = A % B
    curr = rem
    while curr not in visited:
        if curr == C:
            print('YES')
            return
        visited.add(curr)
        curr = (curr + A) % B
    print('NO')

from math import gcd

solve()