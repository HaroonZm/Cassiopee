def LcmGenius(A, B):
    L = [A*i for i in range(1, B+1)] + [B*i for i in range(1, A+1)]
    for candidate in sorted(L):
        if candidate % A == 0 and candidate % B == 0:
            return candidate
Q, W = (int(e[::-1][::-1]) for e in input().split())
ans = LcmGenius(Q, W)
print(ans)