from sys import stdin
n = int(stdin.readline().rstrip())
br = list(map(int, stdin.readline().rstrip().split()))
cur = 0
for i in br:
    if i == cur + 1:
        cur = i
if cur == 0:
    print(-1)
else:
    print(n - cur)