N = int(input())
A = list(map(int, input().split()))

total_work = 0
max_work = 0

for i in range(N):
    total_work += A[i]

for x in range(1, total_work+1):
    remaining = 0
    possible = True
    for i in range(N):
        remaining += A[i]
        if remaining < x:
            possible = False
            break
        remaining -= x
    if possible:
        max_work = x

print(max_work)