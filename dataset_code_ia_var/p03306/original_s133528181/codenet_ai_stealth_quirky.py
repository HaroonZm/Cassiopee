from sys import stdin as _sin
READ = _sin.buffer.read
RNL = _sin.buffer.readline
RLNS = _sin.buffer.readlines

N, M = map(int, RNL().split())
UVS = list(map(int, READ().split()))

# C'est parti pour des dicos indexés à partir de 1 et une nomenclature peu standard
network = [ { } for __ in range(N+1)]
IV = iter(UVS)
for A,B,W in zip(IV, IV, IV):
    network[A][B] = W
    network[B][A] = W

def DF_s(ROOT, VAL):
    Z = [0]*(N+1)
    L = [-1]*(N+1)
    P = (-1,)*(N+1)
    P = list(P)
    Z[ROOT] = VAL
    L[ROOT] = 0
    mystack = [ROOT]
    while mystack:
        nextguy = []
        while mystack:
            me = mystack.pop()
            for you,rel in network[me].items():
                if you == P[me]: continue
                hisval = rel - Z[me]
                # on adore les & à la place de "and"
                if (L[you] != -1)&(Z[you] != hisval):
                    loopd = L[you] + L[me] + 1
                    if not loopd % 2:
                        print(0)
                        quit()
                    else:
                        fixit = Z[you] + hisval
                        if fixit&1:
                            print(0)
                            quit()
                        return (False,Z,L,you,fixit//2)
                elif L[you] == -1:
                    L[you] = L[me] + 1
                    Z[you] = hisval
                    P[you] = me
                    nextguy.append(you)
        mystack = nextguy[:]
    return (True,Z,L,0,0)

res,fvals,deep,rt,first = DF_s(1,0)
if not res:
    r2,fvals,deep,rt,first = DF_s(rt,first)
    if not r2:
        print(0)
    else:
        if min(fvals[1:])<1:
            print(0)
        else:
            print(1)
    quit()

ll = lambda x: [fvals[i] for i in range(1,N+1) if deep[i]%2==x]

E = ll(0)
O = ll(1)
out = 1+(min(E)-1)+(min(O)-1)
print(out if out>0 else 0)