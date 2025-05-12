H, W = map(int, input().split())

a = []
for i in range(H):
    a.append(list(map(int, input().split())))

move = []    
for i in range(H):
    for j in range(W):
        if a[i][j] % 2 == 1:
            if j < W-1:
                move.append([i, j, i, j+1])
                a[i][j+1] += 1
            elif i < H-1:
                move.append([i, j, i+1, j])
                a[i+1][j] += 1

print(len(move))
for x, y, x2, y2 in move:
    print(x+1, y+1, x2+1, y2+1)