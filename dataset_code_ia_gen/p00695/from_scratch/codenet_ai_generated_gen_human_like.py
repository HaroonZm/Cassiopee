def largest_rectangle_in_histogram(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            area = height * width
            if area > max_area:
                max_area = area
        stack.append(i)
    return max_area

def largest_rectangle_in_grid(grid):
    max_area = 0
    heights = [0]*len(grid[0])
    for row in grid:
        for i, val in enumerate(row):
            if val == '1':
                heights[i] += 1
            else:
                heights[i] = 0
        area = largest_rectangle_in_histogram(heights)
        if area > max_area:
            max_area = area
    return max_area

import sys

input_lines = sys.stdin.read().strip('\n ').split('\n')
m = int(input_lines[0])
line_idx = 1

for _ in range(m):
    # skip empty lines between maps if any
    while line_idx < len(input_lines) and input_lines[line_idx].strip() == '':
        line_idx += 1
    grid = []
    for _ in range(5):
        grid.append(input_lines[line_idx].strip().split())
        line_idx += 1
    print(largest_rectangle_in_grid(grid))