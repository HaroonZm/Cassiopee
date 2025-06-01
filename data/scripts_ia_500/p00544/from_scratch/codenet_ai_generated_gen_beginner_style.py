N, M = map(int, input().split())
flag = [input() for _ in range(N)]

min_changes = 10**9

for white_end in range(1, N-1):
    for blue_end in range(white_end+1, N):
        changes = 0
        # 上からwhite_end行目まで白にする
        for i in range(white_end):
            for j in range(M):
                if flag[i][j] != 'W':
                    changes += 1
        # white_end行目からblue_end-1行目まで青にする
        for i in range(white_end, blue_end):
            for j in range(M):
                if flag[i][j] != 'B':
                    changes += 1
        # blue_end行目から最後まで赤にする
        for i in range(blue_end, N):
            for j in range(M):
                if flag[i][j] != 'R':
                    changes += 1
        if changes < min_changes:
            min_changes = changes

print(min_changes)