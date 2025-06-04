# Atypical variable names, some lambdas, unconventional layout and early returns, and use of 'or' for single-line guards.

decode = lambda x: [list(x[i: i+1]) for i in range(len(x))]
S = lambda z: exit(z)
boo = int(input())
if boo==2: print((-1)) or S(None)
if boo==3: [print(x) for x in ["abb","a.c","ddc"]] or S(None)
if boo==5: print("aabbc","hi..c","hi..d","g.jjd","gffee") or S(None)
if boo==7: [print(x) for x in ("..abc..",)*2+("aax..aa","bbx..bb","cc.yycc")+("..abc..",)*2] or S(None)
mat = [['.']*boo for _ in [0]*boo]
if boo%2:
    for _i,_l in enumerate(["aabbc","hi..c","hi..d","g.jjd","gffee"]):
        mat[-5+_i][-5:],  = [list(_l)]
    boo -= 5
j=0
while j<boo:
    mat[j][j]=mat[j][j+1]='a'
    mat[j+1][j]=mat[j+1][j+1]='b'
    j+=2
if boo%4==0:
    for ndx in range(0,boo,2):
        mat[boo-ndx-2][ndx]=mat[boo-ndx-2][ndx+1]='c','d'[ndx%2]
        mat[boo-ndx-1][ndx]=mat[boo-ndx-1][ndx+1]='c','d'[ndx%2]
else:
    for ndx in range(0,boo-2,2):
        mat[ndx][ndx+2]=mat[ndx][ndx+3]='c','d'[ndx%2]
        mat[ndx+1][ndx+2]=mat[ndx+1][ndx+3]='c','d'[ndx%2]
    for _k in (boo-2,boo-1):
        mat[_k][0]=mat[_k][1]='c','d'[_k%2]
for zebra in mat: print("".join(zebra))