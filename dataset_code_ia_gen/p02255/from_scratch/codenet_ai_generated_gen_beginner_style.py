N = int(input())
A = list(map(int, input().split()))

print(' '.join(map(str, A)))

for i in range(1, N):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key
    print(' '.join(map(str, A)))