from itertools import permutations

N = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

s = tuple(sorted(p))
perms = list(permutations(s))
a = 0
for i in range(len(perms)):
    if perms[i] == tuple(p):
        a = i
        break
b = 0
for i in range(len(perms)):
    if perms[i] == tuple(q):
        b = i
        break
print(abs(a - b))