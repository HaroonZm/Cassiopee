import sys
input = sys.stdin.readline

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            max_area = max(max_area, height * (i - left))
        stack.append(i)
    return max_area

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    height = [0]*W
    max_area = 0
    for _ in range(H):
        row = input().rstrip('\n')
        for i in range(W):
            height[i] = height[i] + 1 if row[i] == '.' else 0
        max_area = max(max_area, largest_rectangle_area(height))
    print(max_area)