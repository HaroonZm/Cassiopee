import sys
from functools import reduce

def process_game(a, k):
    while True:
        if a < k:
            return 0
        q, r = divmod(a, k)
        if r == 0:
            return q
        d = q + 1
        steps = ((a - k * q) // d)
        a -= d * steps
        if a < k:
            return 0
        q, r = divmod(a, k)
        if r == 0:
            return q
        a -= d

def main():
    input = sys.stdin.buffer.readline
    N = int(input())
    win = 0

    for _ in range(N):
        a, k = map(int, input().split())
        win ^= process_game(a, k)

    print('Takahashi' if win else 'Aoki')

if __name__ == '__main__':
    main()