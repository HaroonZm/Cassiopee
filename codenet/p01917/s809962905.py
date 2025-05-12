import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
R = list(map(int,input().split()))
SPC = []
S = []
P = []
C = []
ans = 10**5
for i in range(n):
    s,p,c = map(int,input().split())
    S.append(s)
    P.append(p)
    C.append(c)
    SPC.append([s,p,c])

you = list(SPC[0])
for delta in range(1,102-you[0]):
    S[0] = you[0] + delta
    SPC[0][0] = S[0]
    Ssort = sorted(S,reverse = True)
    Psort = sorted(P,reverse = True)
    Csort = sorted(C,reverse = True)
    pointS = {}
    pointP = {}
    pointC = {}
    for r,s,p,c in zip(R,Ssort,Psort,Csort):
        if s not in pointS:pointS[s] = r
        if p not in pointP:pointP[p] = r
        if c not in pointC:pointC[c] = r
    point = [pointS[s]+pointP[p]+pointC[c] for s,p,c in SPC]
    if sorted(point,reverse = True).index(point[0]) != 8:
        ans = min(ans,delta)
        break
S[0] = you[0]
SPC[0] = you.copy()
for delta in range(1,102-you[1]):
    P[0] = you[1] + delta
    SPC[0][1] = P[0]
    Ssort = sorted(S,reverse = True)
    Psort = sorted(P,reverse = True)
    Csort = sorted(C,reverse = True)
    pointS = {}
    pointP = {}
    pointC = {}
    for r,s,p,c in zip(R,Ssort,Psort,Csort):
        if s not in pointS:pointS[s] = r
        if p not in pointP:pointP[p] = r
        if c not in pointC:pointC[c] = r
    point = [pointS[s]+pointP[p]+pointC[c] for s,p,c in SPC]
    if sorted(point,reverse = True).index(point[0]) != 8:
        ans = min(ans,delta)
        break
P[0] = you[1]
SPC[0] = you.copy()
for delta in range(1,102-you[2]):
    C[0] = you[2] + delta
    SPC[0][2] = C[0]
    Ssort = sorted(S,reverse = True)
    Psort = sorted(P,reverse = True)
    Csort = sorted(C,reverse = True)
    pointS = {}
    pointP = {}
    pointC = {}
    for r,s,p,c in zip(R,Ssort,Psort,Csort):
        if s not in pointS:pointS[s] = r
        if p not in pointP:pointP[p] = r
        if c not in pointC:pointC[c] = r
    point = [pointS[s]+pointP[p]+pointC[c] for s,p,c in SPC]
    if sorted(point,reverse = True).index(point[0]) != 8:
        ans = min(ans,delta)
        break

print(ans if ans != 10**5 else 'Saiko')