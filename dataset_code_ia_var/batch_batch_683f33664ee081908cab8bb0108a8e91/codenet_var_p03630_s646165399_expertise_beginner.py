H, W = map(int, input().split())
result = max(H, W)
grid = []
for i in range(H):
    row = input()
    grid.append(row)

rect_list = []
first_row = []
for col in range(W-1):
    first_row.append(0)
rect_list.append(first_row)

for i in range(H-1):
    temp = []
    prev = rect_list[-1]
    for j in range(W-1):
        # Take the 4 corners of the potential rectangle
        corner = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+1][j+1]
        dots = 0
        for k in range(4):
            if corner[k] == '.':
                dots += 1
        if dots % 2 == 0:
            temp.append(prev[j] + 1)
        else:
            temp.append(0)
    rect_list.append(temp)

for row in rect_list[1:]:
    stack = []
    row.append(0)
    for idx in range(len(row)):
        width = -1
        while stack and stack[-1][1] >= row[idx]:
            width, height = stack.pop()
            side = (height + 1) * (idx - width + 1)
            if side > result:
                result = side
        if width != -1:
            stack.append((width, row[idx]))
        else:
            stack.append((idx, row[idx]))

print(result)