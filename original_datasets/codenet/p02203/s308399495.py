N = int(input())
A = [int(x) for x in input().split()]

min = 1
max = N

for i in range(1, N):
    if A[i] <= A[i - 1]:
        min += 1

print(min)
print(max)