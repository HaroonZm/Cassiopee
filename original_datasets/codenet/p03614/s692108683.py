n = int(input())
p = list(map(int, input().split()))

q = [0] * n
for i in range(n):
    if i == p[i]-1:
        q[i] = 1
    if q[i-1] == 1 and q[i] == 1:
        q[i] = 0
print(sum(q))