N = int(input())
A = list(map(int, input().split()))
rev_sum = 0
for i in range(len(A)):
    if A[i] != 0:
        rev_sum += 1 / A[i]
if rev_sum != 0:
    print(1 / rev_sum)
else:
    print(0)