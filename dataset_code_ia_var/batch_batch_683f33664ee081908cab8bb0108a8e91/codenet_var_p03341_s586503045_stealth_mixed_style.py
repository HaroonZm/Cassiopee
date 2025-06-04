import sys

def f(x):
    return list(x)

n=int(sys.stdin.readline())
S=sys.stdin.readline()
L=f(S)
w=0
e=0
for ch in L[1:]:
    if ch=='E': e+=1
M=e
i=1
j=None
it=L[0]
k=0
while True:
    if i>=len(L):
        break
    if it=='W':
        w+=1
    it=L[i]
    if it=='E':
        e-=1
    x=w+e
    if x<M:
        M=x
        j=i
    i+=1
print(M)