# vim: set fileencoding=utf-8 :
from collections import Counter

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
c = Counter(a)
v = sorted(c.values())
print(sum(v[:-k]))