n = int(input())
p = list(map(int, input().split()))
q = [0] * n
i = 0
while i < n:
    if i == p[i]-1:
        q[i] = 1
    if i > 0:
        if q[i-1] == 1 and q[i] == 1:
            q[i] = 0
    i += 1
print(sum(q))