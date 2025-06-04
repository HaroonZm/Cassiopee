H, W = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]

heights = [0]*W
max_area = 0

for row in matrix:
    for i in range(W):
        heights[i] = heights[i] + 1 if row[i] == 0 else 0

    stack = []
    for i in range(W+1):
        h = heights[i] if i < W else 0
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height*width)
        stack.append(i)

print(max_area)