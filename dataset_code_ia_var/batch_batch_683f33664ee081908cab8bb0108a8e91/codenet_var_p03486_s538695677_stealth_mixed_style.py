import sys
from collections import defaultdict

def get_sorted_lists():
    a = sys.stdin.readline().rstrip('\n')
    b = sys.stdin.readline().rstrip('\n')
    l1 = sorted([ch for ch in a])
    l2 = list(b)
    l2.sort(); l2 = l2[::-1]
    return ''.join(l1), ''.join(l2)

class C:
    pass

c = C()
c.s, c.t = get_sorted_lists()

def cmp(x, y):
    return x < y

res = None
for i in range(1):
    if cmp(c.s, c.t):
        res = 'Yes'
        break
    else:
        res = 'No'

print(res)