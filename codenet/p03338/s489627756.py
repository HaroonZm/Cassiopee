n = int(input())
s = input()
import collections
c = 0
for i in range(1,n-1):
    a = set(collections.Counter(s[:i]).keys())
    b = set(collections.Counter(s[i:]).keys())
    c = max(c, len(a & b))
print(c)