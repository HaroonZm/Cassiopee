while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    
    n = int(input())
    lst = [[1] * (a + 1) for _ in range(b + 1)]
    lst[0] = [0] * (a + 1)
    for y in range(2, b + 1):
        lst[y][0] = 0

    for _ in range(n):
        c = list(map(int, input().split()))
        lst[c[1]][c[0]] = 0

    for x in range(1, a + 1):
        for y in range(1, b + 1):
            if lst[y][x] == 0:
                continue
            lst[y][x] = lst[y - 1][x] + lst[y][x - 1]
    print(lst[b][a])