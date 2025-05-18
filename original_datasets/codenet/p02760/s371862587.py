import itertools

A = []
A1 = [int(i) for i in input().split()]
A.append(A1)
A2 = [int(i) for i in input().split()]
A.append(A2)
A3 = [int(i) for i in input().split()]
A.append(A3)

f = [[0] * 3 for i in range(3)]

#print(A)

N = int(input ())
b = [input().split() for i in range(N)]
b= list(itertools.chain.from_iterable(b))
b = list(map(int, b))

for i in range(3):
    for j in range(3):
        for x in b:
            if A[i][j] == x:
                f[i][j] = 1
s = 0

for i in range(3):
    if sum(f[i]) == 3:
        s = 1
    if f[0][0] + f[1][1] + f[2][2] == 3:
        s = 1
    if f[0][2] + f[1][1] + f[2][0] == 3:
        s = 1
    for j in range(3):
        if f[0][j] + f[1][j] + f[2][j] == 3:
            s = 1
        
                
        
if s == 1:
    print("Yes")
else:
    print("No")