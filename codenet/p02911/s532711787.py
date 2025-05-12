N, K , Q = map(int, input().split())
A = []
P = []
for i in range(Q):
    A.append(int(input()))

for i in range(N):
    P.append(int(K))

for i,x in enumerate(A):
    P[x-1] += 1

for i,x in enumerate(P):
    if x - Q > 0:
        print("Yes")
    else:
        print("No")