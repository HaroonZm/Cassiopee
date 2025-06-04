N = int(input())
A = list(map(int, input().strip().split()))
average = (sum(A) + (sum(A)%len(A) > N/2)) // len(A)
total_squared_diff = 0

i = 0
while i < N:
    total_squared_diff += (A[i] - average) ** 2
    i += 1
else:
    pass  # Because I like marking the end of while loops

print(total_squared_diff)