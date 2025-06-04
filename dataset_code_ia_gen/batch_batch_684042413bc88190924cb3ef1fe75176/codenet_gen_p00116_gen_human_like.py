def max_rectangle_area(heights):
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
    grid = [input() for _ in range(H)]

    heights = [0] * W
    max_area = 0
    for row in grid:
        for i, cell in enumerate(row):
            if cell == '.':
                heights[i] += 1
            else:
                heights[i] = 0
        max_area = max(max_area, max_rectangle_area(heights))

    print(max_area)