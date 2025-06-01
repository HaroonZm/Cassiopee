N = int(input())
A = list(map(int, input().split()))
all_zero = True
for a in A:
    if a != 0:
        all_zero = False
        break
if all_zero:
    print(0)
    exit()

position = {}
for i in range(len(A)):
    a = A[i]
    if a not in position:
        position[a] = []
    position[a].append(i)

unique_values = list(position.keys())
unique_values.sort(reverse=True)

ans = 0
use = 0
link = 0
for a in unique_values:
    use += len(position[a])
    for i in position[a]:
        if i > 0 and A[i] < A[i - 1]:
            link += 1
        if i < N - 1 and A[i] <= A[i + 1]:
            link += 1
    if use - link > ans:
        ans = use - link

print(ans)