ans = []

while True:
    n = int(input())
    if n == 0:
        break
    a = sorted(list(map(int, input().split())))
    min_ = a[-1]
    for i in range(1, n):
        min_ = min(min_, a[i] - a[i-1])
    ans.append(min_)

for i in ans:
    print(i)