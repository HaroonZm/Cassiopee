from math import factorial
from sys import stdin

def permutations_count(n, r):
    return factorial(n) // factorial(n - r)

def main():
    N, M = [int(x) for x in stdin.readline().rstrip().split()]
    if N == M:
        x = (factorial(N) % (10 ** 9 + 7)) * (factorial(M) % (10 ** 9 + 7))
        print((x * 2) % (10 ** 9 + 7))
    elif abs(N - M) == 1:
        x = (factorial(N) % (10 ** 9 + 7)) * (factorial(M) % (10 ** 9 + 7))
        print(x % (10 ** 9 + 7))
    else:
        print(0)

if __name__ == "__main__":
    main()