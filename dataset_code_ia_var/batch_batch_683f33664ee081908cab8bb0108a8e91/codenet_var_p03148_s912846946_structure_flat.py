from collections import Counter as ct
n, k = map(int, input().split())
td = []
for i in range(n):
    td.append(list(map(int, input().split())))
tmp_list = []
for x in td:
    tmp_list.append(x[0])
kind = len(ct(tmp_list))
std = sorted(td, key=lambda x: x[1], reverse=True)
dup = []
eat_k = set()
ans = 0
i = 0
while i < k:
    ans += std[i][1]
    if std[i][0] in eat_k:
        dup.append(std[i])
    eat_k.add(std[i][0])
    i += 1
ans += len(eat_k) * len(eat_k)
tmpa = ans
i = k
while i < n:
    if len(dup) == 0:
        break
    if std[i][0] not in eat_k:
        t = dup.pop()
        tmpa -= t[1]
        tmpa += std[i][1]
        tmpa -= len(eat_k) * len(eat_k)
        eat_k.add(std[i][0])
        tmpa += len(eat_k) * len(eat_k)
        if tmpa > ans:
            ans = tmpa
    i += 1
print(ans)