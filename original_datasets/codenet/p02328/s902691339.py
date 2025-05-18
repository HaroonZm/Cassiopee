"""
Pattern - Largest Rectangle in a Histogram
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_3_C&lang=jp

"""
import sys

def solve(heights):
    h_len = len(heights)
    left = [-1] * h_len
    right = [-1] * h_len
    stack = []
    for i in range(h_len):
        if not stack:
            left[i] = 0
        else:
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            left[i] = stack[-1][0]+1 if stack else 0
        stack.append((i, heights[i]))

    stack = []
    for i in range(h_len-1, -1, -1):
        if not stack:
            right[i] = h_len
        else:
            while stack and stack[-1][1] >= heights[i]:
                stack.pop()
            right[i] = stack[-1][0] if stack else h_len
        stack.append((i, heights[i]))

    area = [h*(r-l) for h, l, r in zip(heights, left, right)]
    return max(area)

def main(args):
    _ = input()
    heights = [int(h) for h in input().split()]
    ans = solve(heights)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])