H, W = map(int, input().split())
area = [list(input()) for _ in range(H)]

def calc(area):
    count = 0
    for i in range(H):
        for j in range(W):
            if area[i][j] == '#':
                count += 1
    return count

dist = [[-1 for _ in range(W)] for _ in range(H)]
dist[0][0] = 0
que = [[0, 0]]

dh = [1, 0, -1, 0]
dw = [0, 1, 0, -1]

while len(que) != 0:
    idx = que.pop(0)
    for i in range(4):
        h = idx[0] + dh[i]
        w = idx[1] + dw[i]
        if h >= 0 and h < H and w >= 0 and w < W and dist[h][w] == -1 and area[h][w] != '#':
            que.append([h, w])
            dist[h][w] = dist[idx[0]][idx[1]] + 1

neededWhiteNum = dist[H-1][W-1] + 1
if neededWhiteNum == 0:
    print(-1)
else:
    print(H * W - dist[H-1][W-1] - calc(area) - 1)