import sys
from typing import List

def checkio(matrix: List[List[int]]) -> int:
    # Optimized maximal rectangle in a binary matrix (O(M*N)) using monotonic stack
    def max_rectangle_in_histogram(heights: List[int]) -> int:
        stack, max_area = [], 0
        heights.append(0)  # Sentinel
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()  # Clean up
        return max_area

    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        heights = [h + 1 if cell else 0 for h, cell in zip(heights, row)]
        max_area = max(max_area, max_rectangle_in_histogram(heights))
    return max_area

if __name__ == '__main__':
    input_func = getattr(sys, 'stdin') if sys.version_info[0] < 3 else input
    try:
        n = int(input() if sys.version_info[0] >= 3 else raw_input())
        for _ in range(n):
            data = [[int(e) for e in input().split()] for _ in range(5)]
            print(checkio(data))
            input()
    except EOFError:
        pass