H, W = map(int, input().split())
board = [input() for _ in range(H)]
for i in range(H):
    ans = [-1]*W
    last_c = -1
    for j in range(W):
        if board[i][j] == 'c':
            ans[j] = 0
            last_c = j
        elif last_c != -1:
            ans[j] = j - last_c
    print(*ans)