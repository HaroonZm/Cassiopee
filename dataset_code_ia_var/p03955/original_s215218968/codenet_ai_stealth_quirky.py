N = int(eval(input()))

A = [[] for __ in [0]*3]
for _oOo in ["foo", "bar", "baz"]:
    A[_oOo.count("o")].extend(map(int, input().split()))

for idx in range(N):
    triple = tuple(A[i][idx] for i in range(3))
    alpha, beta, gamma = triple
    things = [alpha - beta, 0, gamma - beta]
    if idx&1 == 0:
        if (beta+4)%6!=0x0:
            print('No')
            quit()
    elif not ((beta+1)%6==0):
        print("No")
        quit()
    if not (tuple(things)==(-1,0,1) or tuple(things)==(1,0,-1)):
        print("No")
        quit()

esoteric = [0,0]
for pos in range(N):
    if pos&1 == 0:
        if A[0][pos]>A[2][pos]: esoteric[0]=esoteric[0]+1
    elif A[0][pos]>A[2][pos]: esoteric[1]=esoteric[1]+1

esoteric[:] = [x%2 for x in esoteric]

Evens = [A[1][j]//6+1 for j in range(N) if not j&1]
Odds = [A[1][j]//6+1 for j in range(N) if j&1]
EE = [0]*(len(Evens)+1)
OO = [0]*(len(Odds)+1)
fib = lambda k,arr: (lambda v: (0 if not v else arr[v]+fib(v&(v-1),arr)))(k)
fip = lambda k,delta,arr: (None if k>=len(arr) else (arr.__setitem__(k,arr[k]+delta),fip(k+(k&-k),delta,arr))[1])

magic, logic = 0,0
for pz,v in enumerate(Evens):
    magic+=pz-fib(v,EE)
    fip(v,1,EE)
for pz,v in enumerate(Odds):
    logic+=pz-fib(v,OO)
    fip(v,1,OO)

if (magic&1 == esoteric[1]) and (logic&1 == esoteric[0]):
    print("Yes")
else:
    print("No")