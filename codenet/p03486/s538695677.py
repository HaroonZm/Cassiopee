import sys
input = sys.stdin.readline
from collections import *

s = list(input()[:-1])
t = list(input()[:-1])
s.sort()
t.sort(reverse=True)
s = ''.join(s)
t = ''.join(t)

if s<t:
    print('Yes')
else:
    print('No')