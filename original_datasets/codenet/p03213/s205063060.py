import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')

def factorize_dict(n):
    b = 2
    fct = defaultdict(lambda: 0)
    while b ** 2 <= n:
        while n % b == 0:
            n //= b
            fct[b] += 1
        b += 1
    if n > 1:
        fct[n] += 1
    return fct

def main():

    N = in_n()

    prime = defaultdict(int)
    for i in range(1, N + 1):
        for k, v in factorize_dict(i).items():
            prime[k] += v

    def num(a):
        return len(list(filter(lambda x: x >= a, prime.values())))

    ans = num(74)
    if num(24) >= 1:
        ans += num(24) * (num(2) - 1)
    if num(14) >= 1:
        ans += num(14) * (num(4) - 1)
    if num(4) >= 2:
        ans += num(4) * (num(4) - 1) // 2 * (num(2) - 2)
    print(ans)

if __name__ == '__main__':
    main()