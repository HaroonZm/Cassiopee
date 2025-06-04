N = int(input())
A = list(map(int, input().split()))

swap_count = 0

for i in range(N):
    mini = i
    for j in range(i, N):
        if A[j] < A[mini]:
            mini = j
    if i != mini:
        A[i], A[mini] = A[mini], A[i]
        swap_count += 1

print(' '.join(map(str, A)))
print(swap_count)