from collections import defaultdict
 
N = int(input())
A = list(map(int, input().split()))
if all(a == 0 for a in A):
    print(0)
    exit()
 
position = defaultdict(list)
for i, a in enumerate(A):
    position[a].append(i)
 
ans = 0
use = 0
link = 0
for a in sorted(set(A), reverse=True):
    use += len(position[a])
    for i in position[a]:
        if i > 0 and A[i] < A[i - 1]:
            link += 1
        if i < N - 1 and A[i] <= A[i + 1]:
            link += 1
    ans = max(ans, use - link)
print(ans)