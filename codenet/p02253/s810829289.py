# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/15/ALDS1_15_C

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x: x[1])
now = -1
ans = 0
for s, t in lst:
    if now < s:
        ans += 1
        now = t
print(ans)