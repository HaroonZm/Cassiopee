N = int(input())
A = input().split()
for i in range(len(A)):
    A[i] = int(A[i])
unique = []
for x in A:
    if x not in unique:
        unique.append(x)
if len(A) == len(unique):
    print('YES')
else:
    print('NO')