from functools import reduce
u=[1,2,3,4,5,6,7,8,9]
a=0
n=tuple(map(int, input().split()))
def check(a,b):
    return a and b
perm_gen = ((x, any(n[i] != -1 and n[i] != x[i] for i in range(9))) for x in __import__('itertools').permutations(u))
for x, invalid in perm_gen:
    if invalid:
        continue
    total = (x[0]+x[2]+x[5]-x[8]) + ((x[1]+x[4]-x[7])*10) + ((x[3]-x[6])*100)
    a += 1 if total == 0 else 0
print(a)