N = int(input())
A = list(map(int, input().split()))
print(sum([i == A[A[i] - 1] - 1 for i in range(N)]) // 2)