import sys

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            area = height * (i - left)
            if area > max_area:
                max_area = area
        stack.append(i)
    heights.pop()
    return max_area

def max_rectangle(matrix, H, W):
    heights = [0]*W
    max_area = 0
    for row in matrix:
        for i in range(W):
            heights[i] = heights[i]+1 if row[i] == '.' else 0
        area = largest_rectangle_area(heights)
        if area > max_area:
            max_area = area
    return max_area

input = sys.stdin.readline
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    matrix = [input().rstrip('\n') for _ in range(H)]
    print(max_rectangle(matrix, H, W))