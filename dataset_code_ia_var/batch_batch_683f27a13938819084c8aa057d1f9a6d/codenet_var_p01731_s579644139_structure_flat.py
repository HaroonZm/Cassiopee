import sys
sys.setrecursionlimit(9999)

n = int(raw_input())
name = []
child = [[] for i in xrange(n)]
for i in xrange(n):
    k = int(raw_input())
    m = raw_input()
    name.append(m)
    if k == 0:
        continue
    child[k - 1].append(i)

stack = [(0, 0)]
while stack:
    i, z = stack.pop()
    print("." * z + name[i])
    # parcourt les enfants en ordre d'origine
    for j in reversed(child[i]):
        stack.append((j, z + 1))