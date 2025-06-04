import sys
input = sys.stdin.readline

H, W = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]

heights = [0]*W
max_area = 0

for row in range(H):
    for col in range(W):
        heights[col] = heights[col] + 1 if matrix[row][col] == 0 else 0

    stack = []
    for i in range(W+1):
        curr_height = heights[i] if i < W else 0
        while stack and heights[stack[-1]] > curr_height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] -1
            area = h*w
            if area > max_area:
                max_area = area
        stack.append(i)

print(max_area)