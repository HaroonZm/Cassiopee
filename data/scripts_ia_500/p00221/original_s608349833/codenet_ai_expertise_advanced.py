from sys import stdin
from collections import deque

def fb_gen():
    for i in range(1, 10**18):
        yield "FizzBuzz" if i % 15 == 0 else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else str(i)

def main():
    input = stdin.readline
    while (m := input().strip()):
        if not m:
            break
        m, n = map(int, m.split())
        if (m, n) == (0, 0):
            break
        players = deque(range(1, m + 1))
        fb = fb_gen()
        for _ in range(n):
            p = input().strip()
            if p != next(fb):
                if len(players) > 1:
                    players.popleft()
            else:
                players.rotate(-1)
        print(*sorted(players))

if __name__ == '__main__':
    main()