H, W = map(int, input().split())
matrix = []
for _ in range(H):
    row = list(map(int, input().split()))
    matrix.append(row)

max_side = 0

for i in range(H):
    for j in range(W):
        if matrix[i][j] == 0:
            side = 1
            while True:
                if i + side > H or j + side > W:
                    break
                all_zero = True
                for x in range(i, i + side):
                    for y in range(j, j + side):
                        if matrix[x][y] != 0:
                            all_zero = False
                            break
                    if not all_zero:
                        break
                if all_zero:
                    side += 1
                else:
                    break
            if side -1 > max_side:
                max_side = side -1

print(max_side * max_side)