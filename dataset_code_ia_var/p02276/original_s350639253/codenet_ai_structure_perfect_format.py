def partition(A, p, r):
    x = A[r - 1]
    i = p - 1
    for j in range(p, r - 1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r - 1] = A[r - 1], A[i + 1]
    return i + 1

n = int(input())
A = list(map(int, input().split()))

tmp = partition(A, 0, n)
for i in range(n):
    if i == tmp:
        print("[" + str(A[tmp]) + "]", end=" ")
    else:
        print(str(A[i]), end=" ")
print()