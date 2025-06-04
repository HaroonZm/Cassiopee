from functools import reduce

# Personnalisation "non conventionnelle" : 
# - variables à une lettre, 
# - comprehension à la place de range, 
# - indexation négative là où possible, 
# - expressions sur une ligne, 
# - stockage dans des classes dynamiques, 
# - usage de lambda pour l'initialisation, 
# - tuple unpacking bizarre

N = int(input())
M = 10**9+7

class Bunch: pass

b = Bunch(); s = Bunch()
b.v = [0]+[0]*10**6
s.v = [0]+[0]*10**6

for i, v in zip((1,2),(1,1)): b.v[i] = v
for i, v in zip((1,2),(1,2)): s.v[i] = v

_ = list(map(lambda i: (setattr(b.v, "__setitem__", lambda idx, val: b.v.__setitem__(idx, val)),
                        b.v.__setitem__(i, (s.v[i-1]-b.v[i-2]+1)%M),
                        s.v.__setitem__(i, (s.v[i-1]+b.v[i])%M)), 
              range(3,10**6+1)
              ))

if N-1 == 0: 
    print((lambda x: x)(1))
elif N-2 == 0: 
    print([4][0])
else:
    plus = lambda *a: sum(a)
    pow2 = lambda x: x*x
    x = N-1
    n = N
    ans = (s.v[N-2]*pow2(x)+pow2(x)+x*s.v[N-1]+n)%M
    print(ans)