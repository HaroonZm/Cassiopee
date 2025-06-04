N = int(input())
D = [int(input()) for _ in range(N)]
A = [D[0]]
for d in D:
    if d not in A:
        A.append(d)
print(len(A))