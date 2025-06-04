import sys

def funky_ctr(seq):
    d = {}
    for x in seq:
        d[x] = d.get(x, 0) + 1
    return d

def ctr_and(c1, c2):
    return {k: min(c1[k], c2[k]) for k in c1 if k in c2 and min(c1[k], c2[k]) > 0}

Z=lambda:sys.stdin.readline().rstrip('\n')
n = int(Z())
s = Z()

righty = funky_ctr(s)
lefty = {}

res = -float('inf')
for idx, ch in enumerate(s):
    lefty[ch] = lefty.get(ch, 0) + 1
    righty[ch] -= 1
    if righty[ch]==0:
        del righty[ch]
    shared = ctr_and(lefty, righty)
    res = res if res > len(shared) else len(shared)
print(res)