def f(_): return list(map(int, _.split()))
a, b = f(input())
C = [f(input()) for __ in range(a)]
X = [[] for _ in range(8)]
for i in range(len(C)):
    x, y, z = C[i]
    X[0]+=[ x+y+z ]
    X[1].append( x+y-z )
    X[2].extend( [x-y+z] )
    X[3].append( x-y-z )
    X[4].append( -x+y+z )
    X[5]+=[ -x+y-z ]
    X[6]+=[ -x-y+z ]
    X[7].append( -x-y-z )
list(map(lambda lst: lst.sort(reverse=1), X))
r=0
i=0
while i<8:
    s = 0
    for e in range(b): s+=X[i][e]
    if s>r: r=s
    i+=1
print(r)