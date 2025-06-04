import sys

def foo():
    return map(int, sys.stdin.readline().split())

n, m = foo()
s = (input())[::-1] + '1' * m

if m >= n:
    print(n); sys.exit()

result = []; idx = 0; ptr = 0

class Holder:
    pass

holder = Holder()
holder.q = []
holder.push = holder.q.insert
holder.pop = holder.q.pop

def step(i, j):
    for k in range(i + m, j, -1):
        if s[k] == '0': return k
    return -1

while idx < n:
    flag = False
    k = step(idx, ptr)
    if k != -1:
        flag = True
    ptr = idx + m
    holder.push(0, k - idx)
    idx = k
    if not flag:
        print(-1)
        quit()

for x in holder.q:
    result.append(str(x))
print(' '.join(result))