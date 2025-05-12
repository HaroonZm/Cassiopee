import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')

def main():
    N, M = in_nn()
    d = defaultdict(int)
    for x in in_na():
        d[x] += 1

    ans = 'YES'
    for i in range(1, N + 1):
        if d[i] % 2 == 1:
            ans = 'NO'
            break

    print(ans)

if __name__ == '__main__':
    main()