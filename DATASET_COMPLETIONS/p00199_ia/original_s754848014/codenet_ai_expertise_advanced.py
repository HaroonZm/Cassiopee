INF = 10**10

def place_A(chair):
    for i, c in enumerate(chair):
        if c == "#":
            chair[i] = "A"
            break

def place_B(chair):
    for i in range(len(chair) - 1, -1, -1):
        if chair[i] == "#" and not (
            (i > 0 and chair[i-1] == "A") or (i < len(chair) - 1 and chair[i+1] == "A")
        ):
            chair[i] = "B"
            return
    place_A(chair)  # fallback to first available seat

def place_C(chair):
    n = len(chair)
    if chair.count("#") == n:
        chair[n//2] = "C"
        return
    for i, c in enumerate(chair):
        if c != "#":
            for ni in (i+1, i-1):
                if 0 <= ni < n and chair[ni] == "#":
                    chair[ni] = "C"
                    return

def place_D(chair):
    n = len(chair)
    if chair.count("#") == n:
        chair[0] = "D"
        return

    distmap = [INF] * n
    dist = INF

    for i in range(n):
        if chair[i] != "#":
            dist = 0
        else:
            dist = dist + 1 if dist != INF else INF
        distmap[i] = dist

    dist = INF
    for i in range(n - 1, -1, -1):
        if chair[i] != "#":
            dist = 0
        else:
            dist = dist + 1 if dist != INF else INF
        distmap[i] = min(distmap[i], dist)

    max_distance = max((d for d, c in zip(distmap, chair) if c == "#"), default=-1)
    for i, d in enumerate(distmap):
        if d == max_distance and chair[i] == "#":
            chair[i] = "D"
            break


while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    chair = ["#"] * N
    handlers = {"A": place_A, "B": place_B, "C": place_C, "D": place_D}

    for _ in range(M):
        cmd = input()
        handlers[cmd](chair)

    print("".join(chair))