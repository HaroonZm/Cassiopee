import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

def square(P):
    heights = []
    stack = []
    for i in range(len(P)):
        v = P[i]
        if len(stack) == 0:
            stack.append((i, v))
            continue
        if v > stack[-1][1]:
            stack.append((i, v))
        elif v < stack[-1][1]:
            k = i - 1
            while len(stack) > 0 and v < stack[-1][1]:
                a = stack.pop()
                heights.append((k - a[0] + 1) * a[1])
            stack.append((a[0], v))
    while len(stack) > 0:
        a = stack.pop()
        heights.append((n - a[0]) * a[1])
    return max(heights)

print(square(li))