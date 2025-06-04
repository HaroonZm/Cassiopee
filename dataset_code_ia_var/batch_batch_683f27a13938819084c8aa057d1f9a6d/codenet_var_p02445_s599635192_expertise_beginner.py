n = int(input())
A = input().split()
for i in range(n):
    A[i] = int(A[i])

q = int(input())
for i in range(q):
    values = input().split()
    b = int(values[0])
    e = int(values[1])
    t = int(values[2])

    for j in range(e - b):
        temp = A[b + j]
        A[b + j] = A[t + j]
        A[t + j] = temp

for x in A:
    print(x, end=' ')