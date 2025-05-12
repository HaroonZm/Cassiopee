import re
n = int(input())
s = input()
res = 10**10
res = min(res, len(re.search(r'^<*', s).group()))
res = min(res, len(re.search(r'>*$', s).group()))
print(n-res)