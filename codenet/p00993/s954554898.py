A=[]
B=range(2, 1600)
while(B[0]<40):
    b=B.pop(0)
    A.append(b)
    B=[x for x in B if x%b!=0]
A+=B
C=range(2,1600)
for b in A:
    C=[b if c%b==0 else c for c in C]
N=reduce(lambda a,b: a*b, A)+2
print N
q=int(raw_input())
for i in range(q):
    print C[i]