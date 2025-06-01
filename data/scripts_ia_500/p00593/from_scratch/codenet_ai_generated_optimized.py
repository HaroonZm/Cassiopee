case_num = 1
while True:
    N = int(input())
    if N == 0:
        break
    res = [[0]*N for _ in range(N)]
    count = 1
    for s in range(2*N-1):
        if s % 2 == 0:
            x = min(s, N-1)
            y = s - x
            while x >= 0 and y < N:
                res[x][y] = count
                count += 1
                x -= 1
                y += 1
        else:
            y = min(s, N-1)
            x = s - y
            while y >= 0 and x < N:
                res[x][y] = count
                count += 1
                x += 1
                y -= 1
    print(f"Case {case_num}:")
    for row in res:
        print(''.join(f"{v:3d}" for v in row))
    case_num += 1