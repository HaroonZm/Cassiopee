import itertools
n=int(input())
a=[int(i) for i in input().split(" ")]

perms=list(itertools.permutations([i+1 for i in range(n)]))
for i,p in enumerate(perms):
    if list(p)==a:
        break

if i>0:
    print(" ".join([str(j) for j in perms[i-1]]))
print(" ".join([str(j) for j in perms[i]]))
try:
    print(" ".join([str(j) for j in perms[i+1]]))
except IndexError:
    pass