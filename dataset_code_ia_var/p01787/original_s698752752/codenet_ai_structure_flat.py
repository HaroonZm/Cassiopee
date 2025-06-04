import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# Entrée des trois lignes puis traitement à plat sans fonctions :

s1 = sys.stdin.readline().split()
a1 = []
for i1 in range(len(s1)-1):
    if i1 % 2 == 0:
        a1.append(s1[i1])
    else:
        a1.append(int(s1[i1]))

s2 = sys.stdin.readline().split()
a2 = []
for i2 in range(len(s2)-1):
    if i2 % 2 == 0:
        a2.append(s2[i2])
    else:
        a2.append(int(s2[i2]))

s3 = sys.stdin.readline().split()
a3 = []
for i3 in range(len(s3)-1):
    if i3 % 2 == 0:
        a3.append(s3[i3])
    else:
        a3.append(int(s3[i3]))

# Compression 
tmpa = a1[:2]
i = 2
while i < len(a1):
    if a1[i] == tmpa[-2]:
        tmpa[-1] += a1[i+1]
    else:
        tmpa += a1[i:i+2]
    i += 2
a1c = tmpa

tmpb = a2[:2]
i = 2
while i < len(a2):
    if a2[i] == tmpb[-2]:
        tmpb[-1] += a2[i+1]
    else:
        tmpb += a2[i:i+2]
    i += 2
a2c = tmpb

tmpc = a3[:2]
i = 2
while i < len(a3):
    if a3[i] == tmpc[-2]:
        tmpc[-1] += a3[i+1]
    else:
        tmpc += a3[i:i+2]
    i += 2
a3c = tmpc

a = a1c
b = a2c
c = a3c

r = []
ff = True
if len(b) == 2:
    b0 = b[0]
    b1 = b[1]
    i = 0
    while i < len(a):
        if a[i] == b0:
            while a[i+1] >= b1 and ff:
                r += c
                a[i+1] -= b1
                ff = False
            if a[i+1] > 0:
                r += a[i:i+2]
        else:
            r += a[i:i+2]
        i += 2
else:
    i = 0
    al = len(a)
    bl = len(b)
    be = bl - 2
    while i < al:
        f = True
        for j in range(0,bl,2):
            ii = i + j
            if al <= ii or a[ii] != b[j] or (a[ii+1] < b[j+1] if j in [0, be] else a[ii+1] != b[j+1]) or not ff:
                f = False
                break
        if f:
            for j in range(0,bl,2):
                ii = i + j
                a[ii+1] -= b[j+1]
        if a[i+1] > 0:
            r += a[i:i+2]
        if f:
            r += c
            ff = False
        i += 2

r += ['$']

# Compression plat de sortie
s = r
res = s[:2]
i = 2
while i < len(s):
    if s[i] == res[-2]:
        res[-1] += s[i+1]
    else:
        res += s[i:i+2]
    i += 2

print(' '.join(map(str,res)))