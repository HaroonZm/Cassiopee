N = int(input())
A = list(map(int, input().split()))
min_val = min(A)
min_idx = -1
for i in range(len(A)):
    if A[i] == min_val:
        min_idx = i
        break
print(min_idx + 1)