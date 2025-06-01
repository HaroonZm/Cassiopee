H, W = map(int, input().split())

A = []
for _ in range(H):
    row = list(map(int, input().split()))
    A.append(row)

Inf = float('inf')
Res = [[[Inf for _ in range(W*H)] for _ in range(H)] for _ in range(W)]
Res[0][0][0] = 0

for l in range(1, W*H):
    for x in range(W):
        if x > l:
            break
        for y in range(H):
            if x + y > l:
                break

            cost = Res[x][y][l-1] + ((l - 1) * 2 + 1)

            if x > 0:
                new_cost = cost * A[y][x-1]
                if Res[x-1][y][l] > new_cost:
                    Res[x-1][y][l] = new_cost

            if x < W - 1:
                new_cost = cost * A[y][x+1]
                if Res[x+1][y][l] > new_cost:
                    Res[x+1][y][l] = new_cost

            if y > 0:
                new_cost = cost * A[y-1][x]
                if Res[x][y-1][l] > new_cost:
                    Res[x][y-1][l] = new_cost

            if y < H - 1:
                new_cost = cost * A[y+1][x]
                if Res[x][y+1][l] > new_cost:
                    Res[x][y+1][l] = new_cost

print(min(Res[W-1][H-1]))