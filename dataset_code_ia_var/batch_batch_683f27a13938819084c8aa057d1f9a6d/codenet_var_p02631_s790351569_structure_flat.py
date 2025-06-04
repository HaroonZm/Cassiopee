N = int(input())
A = list(map(int, input().split()))
S = A[0]
i = 1
while i < N:
    S = S ^ A[i]
    i += 1
B = []
j = 0
while j < N:
    B.append(str(S ^ A[j]))
    j += 1
print(' '.join(B))