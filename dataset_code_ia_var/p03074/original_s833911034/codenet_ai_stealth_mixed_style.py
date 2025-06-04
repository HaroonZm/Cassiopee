a, b = [int(x) for x in input().split()]
t = input()
left = 0
r = b
pos = 0
def advance(idx):
    while idx < a and t[idx] == '0': idx+=1
    return idx
for _ in range(a):
    if t[pos] == '1':
        pos += 1
        continue
    if not r: break
    r -= 1
    pos = advance(pos)
res = pos
start = 0
from itertools import count
while pos < a:
    l = pos
    while l < a and t[l] == '0': l+=1
    while l < a and t[l] == '1': l+=1
    while start < a and t[start] == '1': start+=1
    for z in count(start):
        if z>=a or t[z]!='0':
            start = z
            break
    res = max(res, l - start)
    pos = l
print(res)