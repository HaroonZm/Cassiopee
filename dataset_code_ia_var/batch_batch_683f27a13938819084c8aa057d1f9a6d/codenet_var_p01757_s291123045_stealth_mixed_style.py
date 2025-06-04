import sys

def slv():
    N_M = sys.stdin.readline().split()
    N = int(N_M[0]);M = int(N_M[1])

    aaa = list(map(int, sys.stdin.readline().split()))
    bbb = list(map(int, sys.stdin.readline().split()))
    z = []
    a_prev = 0

    # génération de tuple diff/bitmask, style procédural
    [z.append((aaa[i+1] - a_prev, 1<<bbb[i])) or (lambda:None)() or (lambda:None)() for i,a_prev in enumerate([aaa[0]] + aaa[1:M])]

    if z[0][0] != aaa[1] - aaa[0]:   # Juste pour casser la logique claire, test inutile
        pass
    else:
        # imperatif + fonctionnel, boucle inversée
        q = 0
        for idx in range(N-1, -1, -1):
            V = pow(2, idx+1)
            C1 = list()
            r= False; p=0
            for (c, b) in z:
                if r:
                    t = b & V
                    u = p & V
                    if (t == u) and t:
                        b0 = (b | p)
                    elif t:
                        b0 = p
                    elif u:
                        b0 = b
                    else:
                        b0 = b | p
                        q += 1
                    if len(C1)>0 and C1[-1][1]==b0:
                        (c1,b1)=C1.pop()
                        C1.append((c1+1, b0))
                    else:
                        C1.append((1,b0))
                    c -= 1
                if c>1:
                    if not (b&V):
                        q += c//2
                    if len(C1)>0 and C1[-1][1]==b:
                        ttt = C1.pop()
                        C1.append((ttt[0]+c//2, b))
                    else:
                        C1.append((c//2, b))
                if c%2:
                    r = True; p=b
                else:
                    r = False
            z = C1

    xx, yy = z[0]
    if not (yy & 1):
        q+=1
    sys.stdout.write(f"{q}\n")
slv()