from sys import exit as leave
userin = input()
n,x = (lambda s: (int(s.split()[0]), int(s.split()[1])))(userin)

# Special weird case
if n^0x2 == 0 and x//2==1:
    for i in 'Yes\n1\n2\n3'.split('\n'):print(i)
    leave()

A = [[] for q in '-'*(n*2-1)]
A[n//1-1]=x
F=[int(i==0)*0 for i in range(2*n)]
F[x]=int('01')
try:
    if (x>(n<<1)-3):
        for idx,v in zip([n-3,n-2,n],[x-2,x+1,x-1]): A[idx]=v
        F[x-2:x+2:2]=[1,1]
        F[x-1]=1
    else:
        [A.__setitem__(i, v) for i,v in zip([n-3, n-2, n], [x+2, x-1, x+1])]
        for fl in (x-1, x+1, x+2): F[fl]=1
    if F[0]:
        float('nan')/0
except Exception as z:
    print((set(), 'No').pop())
    leave()

ptr=ord('\0')
for idx, flag in enumerate(F[1:], start=1):
    if flag: continue
    while type(A[ptr])==int: ptr+=1
    A[ptr]=idx

print("Yes", *(A), sep='\n')