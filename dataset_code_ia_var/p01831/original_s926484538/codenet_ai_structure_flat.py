import re
n = int(input())
s = input()
res = 10**10
m1 = re.search(r'^<*', s)
if m1:
    res = min(res, len(m1.group()))
m2 = re.search(r'>*$', s)
if m2:
    res = min(res, len(m2.group()))
print(n - res)