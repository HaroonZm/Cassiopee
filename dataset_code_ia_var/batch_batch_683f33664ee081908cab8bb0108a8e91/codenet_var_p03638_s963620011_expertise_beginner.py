h, w = input().split()
h = int(h)
w = int(w)
n = int(input())
data = input().split()
for i in range(len(data)):
    data[i] = int(data[i])

ans = []
for i in range(h):
    row = []
    for j in range(w):
        row.append(0)
    ans.append(row)

cur_row = 0
cur_col = 0
direction = 1  # 1 for right, 2 for left
color = 1
for amount in data:
    for a in range(amount):
        ans[cur_row][cur_col] = color
        if direction == 1:
            if cur_col == w - 1:
                direction = 2
                cur_row += 1
            else:
                cur_col += 1
        else:
            if cur_col == 0:
                direction = 1
                cur_row += 1
            else:
                cur_col -= 1
    color += 1

for i in range(h):
    for j in range(w):
        print(ans[i][j], end=' ')
    print()