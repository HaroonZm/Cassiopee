v = int(input())
P = dict(); Q = dict()

for z in range(v):
    *a, b = input().split()
    Q[a[0]] = z
    P[z] = int(b)

Y = input()
result = sum(map(lambda x: P[x], range(Q[Y], v)))
if Q[Y] in P:
    result -= P[Q[Y]]
print(result)