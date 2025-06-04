from sys import stdin

def trailing_zeros(n: int) -> int:
    return (n & -n).bit_length() - 1

N = int(stdin.readline())

best = max(range(1, N+1), key=trailing_zeros)
print(best)