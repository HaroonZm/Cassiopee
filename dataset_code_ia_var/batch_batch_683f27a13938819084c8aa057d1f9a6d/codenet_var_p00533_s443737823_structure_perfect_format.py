h, w = map(int, input().split())
cloud = [[c for c in input()] for _ in range(h)]
flag = 0
cnt = 0
for i in range(h):
    for j in range(w):
        if j == w - 1 and flag == 0 and cloud[i][j] == '.':
            print(-1, end='')
        elif j == w - 1 and cloud[i][j] == 'c':
            print(0, end='')
            flag = 1
            cnt = 0
        elif j == w - 1 and cloud[i][j] == '.':
            cnt += 1
            print(cnt, end='')
        elif flag == 0 and cloud[i][j] == '.':
            print(-1, end=' ')
        elif cloud[i][j] == 'c':
            print(0, end=' ')
            flag = 1
            cnt = 0
        else:
            cnt += 1
            print(cnt, end=' ')
    print()
    cnt = 0
    flag = 0