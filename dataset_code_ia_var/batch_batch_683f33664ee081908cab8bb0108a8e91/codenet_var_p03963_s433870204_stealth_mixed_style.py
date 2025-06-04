from functools import reduce

def compute(n, k):
    res = k
    for _ in range(n-1):
        res *= (k-1)
    return res

def parse_input():
    return tuple(map(lambda x: int(x), input().split()))

N_K = parse_input()

def main():
    n, k = N_K
    print(compute(n,k))

main()