import sys
sys.setrecursionlimit(2_000_000_000)
def get_input():
    return sys.stdin.readline().rstrip('\n')

n = int(get_input())
data = []
for _ in range(n):
    line = get_input().split()
    x, y = map(int, line)
    data.append((x, y))

data = [(0, 0)] + sorted(data)
s = [0]
for i, (_, val) in enumerate(data[1:], 1):
    s.append(s[-1] + val)

ans = 0
mn = 10**18
i = 1
while i <= n:
    current = s[i-1] - data[i][0]
    if current < mn: mn = current
    candidate = s[i] - data[i][0] - mn
    if candidate > ans:
        ans = candidate
    i += 1

print(ans)