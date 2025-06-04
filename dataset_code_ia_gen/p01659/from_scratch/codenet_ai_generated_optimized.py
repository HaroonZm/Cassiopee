import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

stack = []
res = 0
for h in a:
    count = 1
    while stack and stack[-1][0] > h:
        res += stack[-1][1]
        stack.pop()
    if stack and stack[-1][0] == h:
        stack[-1] = (h, stack[-1][1] + 1)
    else:
        stack.append((h, 1))
res += sum(c for _, c in stack)
print(res)