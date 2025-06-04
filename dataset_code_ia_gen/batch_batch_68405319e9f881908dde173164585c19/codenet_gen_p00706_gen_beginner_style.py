while True:
    N = int(input())
    if N == 0:
        break
    W, H = map(int, input().split())
    field = [[0]*(W+1) for _ in range(H+1)]
    for _ in range(N):
        x, y = map(int, input().split())
        field[y][x] = 1
    S, T = map(int, input().split())

    max_trees = 0
    for top in range(1, H - T + 2):
        for left in range(1, W - S + 2):
            count = 0
            for y in range(top, top + T):
                for x in range(left, left + S):
                    count += field[y][x]
            if count > max_trees:
                max_trees = count
    print(max_trees)