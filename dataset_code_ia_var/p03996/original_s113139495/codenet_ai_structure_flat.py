n, m = map(int, input().split())
q = int(input())
a = list(map(int, input().split()))

sa = set(a)
seen = set()
r = []
for n_ in a[::-1]:
    if n_ not in seen:
        r.append(n_)
        seen.add(n_)
for i in range(m):
    if (i+1) not in sa:
        r.append(i+1)

count = [0] * (m+1)
count[0] = n
table = [-1] * (m+1)
for i in range(len(r)):
    table[r[i]] = i

for aa in a[::-1]:
    index = table[aa]
    if 0 < count[index]:
        count[index] -= 1
        count[index+1] += 1

to = m
for i in range(m):
    if 0 < count[i]:
        to = i
        break

ok = True
rr = r[to:]
for i in range(1, len(rr)):
    if rr[i-1] > rr[i]:
        ok = False
        break

if ok:
    print('Yes')
else:
    print('No')