f = [[1, 1], [0, 1]]

N = int(input())
A_str = input().split()
A = []
for x in A_str:
    if x == 'T':
        A.append(1)
    else:
        A.append(0)

v = A[0]

for i in range(1, N):
    v = f[v][A[i]]

if v:
    print('T')
else:
    print('F')