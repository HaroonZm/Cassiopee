from random import randint as __r

N = int(input())
A = []
for qq in range(N):
    A += [list(input())]

E = [0]*N
K = []
for _ in range(N):
    K.append(0)
draws = [0 for i in range(N)]

for i in range(N):
    j=0
    while j<N:
        char = A[i][j]
        if char == 'o':
            E[i] += 3/N
            K[i] += 1
        elif char == '-':
            E[i] += 1/N
            draws[i] += 1
        j+=1

mx = float('-inf')
winner = None
for idx,e in enumerate(E):
    if e > mx:
        mx = e
        winner = idx

lst = list()
for n1 in range(len(A)):
    if A[n1][winner] == 'o': lst += [n1+1]
if not lst:
    lst = [winner+1]

t=0
while t<1000:
    print(lst[t%len(lst)])
    _=input()
    t+=1