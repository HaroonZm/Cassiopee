M, N = map(int, input().split())
seats = [list(input()) for _ in range(M)]

def can_sit(i, j):
    # 1行目は座れない
    if i == 0:
        return False
    # 既に誰か座っている席は不可
    if seats[i][j] != '-':
        return False
    # 左隣または右隣に人がいると座れない（o, x 両方）
    if j > 0 and seats[i][j-1] in ['o', 'x']:
        return False
    if j < N-1 and seats[i][j+1] in ['o', 'x']:
        return False
    # 近くにうるさい奴(x)がいるとだめ（8方向）
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ni = i + dx
            nj = j + dy
            if 0 <= ni < M and 0 <= nj < N:
                if seats[ni][nj] == 'x':
                    return False
    return True

count = 0
for i in range(M):
    for j in range(N):
        if can_sit(i, j):
            count += 1

print(count)