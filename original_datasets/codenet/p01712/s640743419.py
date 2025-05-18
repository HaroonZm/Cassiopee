N, W, H = map(int, input().split())
row, col = [0] * (H + 1), [0] * (W + 1)
for _ in range(N):
    x, y, w = map(int, input().split())
    row[max(0, y - w)] += 1
    row[min(H, y + w)] -= 1
    col[max(0, x - w)] += 1
    col[min(W, x + w)] -= 1
flag1 = flag2 = True
for i in range(H):
    row[i + 1] += row[i]
    flag1 &= row[i] > 0
if flag1:
    print("Yes")
    quit()
for i in range(W):
    col[i + 1] += col[i]
    flag2 &= col[i] > 0
if flag2:
    print("Yes")
else:
    print("No")