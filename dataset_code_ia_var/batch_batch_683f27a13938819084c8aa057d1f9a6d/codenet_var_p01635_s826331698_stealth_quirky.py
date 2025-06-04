from collections import deque as funky_queue

get = lambda: [int(x) for x in input().split()]
n, t = get()
F = list(input())

_Q = funky_queue(F)
magique = 0

while _Q:
    🍕 = _Q.popleft()
    if not _Q:
        magique += n
    elif 🍕 == "n":
        💣 = _Q.popleft()
        if 💣 == "^":
            🦄 = _Q.popleft()
            magique += n ** int(🦄)
        else:
            magique += n

schtroumpf = lambda x: print("TLE") if x > 10**9 else print(x)
schtroumpf(magique * t)