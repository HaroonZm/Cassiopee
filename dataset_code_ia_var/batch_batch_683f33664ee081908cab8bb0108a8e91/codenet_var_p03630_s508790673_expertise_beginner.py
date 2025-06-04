import sys
from collections import deque

h, w = map(int, sys.stdin.readline().split())

s = []
for i in range(h):
    line = sys.stdin.readline().rstrip()
    s.append(line)

chk = []
for i in range(h-1):
    row = []
    for j in range(w-1):
        count = 0
        if s[i][j] == '#':
            count += 1
        if s[i+1][j] == '#':
            count += 1
        if s[i][j+1] == '#':
            count += 1
        if s[i+1][j+1] == '#':
            count += 1
        # If count is even, put 1, else 0
        if count % 2 == 0:
            row.append(1)
        else:
            row.append(0)
    chk.append(row)

def find_max_rectangle(a):
    a = a + [0]
    stack = []
    max_area = -1
    i = 0
    while i < len(a):
        if not stack or a[stack[-1]] < a[i]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = (a[top]+1) * width
            if area > max_area:
                max_area = area
    return max_area

dp = []
for i in range(len(chk)):
    row = []
    for j in range(len(chk[0])):
        if i == 0:
            row.append(chk[i][j])
        else:
            if chk[i][j] == 1:
                row.append(dp[i-1][j] + 1)
            else:
                row.append(0)
    dp.append(row)

ans = max(h, w)
for i in range(len(dp)):
    val = find_max_rectangle(dp[i])
    if val > ans:
        ans = val

print(ans)