import sys
from functools import lru_cache
from itertools import islice

input = sys.stdin.readline

NUM = 100
MOD = 10**16 + 61
BASE = 12345
BASE_INV = pow(BASE, MOD - 2, MOD)

power = [pow(BASE, n, MOD) for n in range(NUM)]
power_inv = [pow(BASE_INV, n, MOD) for n in range(NUM)]

def rollhash(s):
    acc = 0
    res = [0]
    for i, c in enumerate(s):
        acc = (acc + power[i] * ord(c)) % MOD
        res.append(acc)
    return res

def debug(var, name="hoge"):
    print(f"{type(var)} {name} = {var!r}", file=sys.stderr)

def main():
    vowels = {'a', 'i', 'u', 'e', 'o'}
    while True:
        N = int(input())
        if N == 0:
            break

        S = []
        for _ in range(N):
            s = input().rstrip()
            n = s[0] + ''.join(s[i+1] for i in range(len(s)-1) if s[i] in vowels)
            S.append(n)

        S.sort(key=len, reverse=True)

        if len(set(S)) < N:
            print(-1)
            continue

        for k in range(1, 51):
            seen = {s[:k] for s in S}
            if len(seen) == N:
                print(k)
                break

if __name__ == "__main__":
    main()