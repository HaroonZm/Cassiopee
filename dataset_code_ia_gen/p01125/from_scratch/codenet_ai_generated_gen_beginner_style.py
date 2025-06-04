while True:
    N = int(input())
    if N == 0:
        break
    gems = set()
    for _ in range(N):
        x, y = map(int, input().split())
        gems.add((x, y))
    M = int(input())
    x, y = 10, 10
    collected = set()
    if (x, y) in gems:
        collected.add((x, y))
    for _ in range(M):
        d, l = input().split()
        l = int(l)
        for _ in range(l):
            if d == 'N':
                y += 1
            elif d == 'E':
                x += 1
            elif d == 'S':
                y -= 1
            elif d == 'W':
                x -= 1
            if (x, y) in gems:
                collected.add((x, y))
    if len(collected) == len(gems):
        print("Yes")
    else:
        print("No")