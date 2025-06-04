from operator import xor

def get(n: int) -> int:
    return [n, 1, n + 1, 0][n & 3]

A, B = map(int, input().split())

print(xor(get(A - 1), get(B)))