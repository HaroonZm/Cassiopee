import sys
read = sys.stdin.read
readline = sys.stdin.readline

def isinsums(x, lst):
    s = sum(lst)
    t = (s + x) // 2
    if s == 0 and x == 0:
        return True
    if (s - x) % 2 or t < 0:
        return False
    t = (s + x) // 2
    m1 = (1 << (t + 1)) - 1
    m2 = 1 << t
    sums = 0
    for e in lst:
        sums = (sums | (1 + sums) << e) & m1
    sums |= 1
    if sums & m2 > 0:
        return True
    return False

s = readline().strip()
x, y = map(int, readline().split())

s = s.replace('TF', 'T F')
s = s.replace('FT', 'F T')
bs = s.split()
if bs[0][0] == 'F':
    x -= len(bs[0])
    del bs[0]

xy = [[], []]
f = 0
for i, e in enumerate(bs):
    if not i % 2:
        l = len(e)
    else:
        f ^= l % 2
        xy[f].append(len(e))

if isinsums(x, xy[0]) and isinsums(y, xy[1]):
    print('Yes')
else:
    print('No')