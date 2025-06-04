import re

n = int(raw_input())
s = raw_input()
m1 = re.search(r'^<*', s)
m2 = re.search(r'>*$', s)
v1 = m1.end() - m1.start()
v2 = m2.end() - m2.start()
print n - min([v1, v2])