N = int(raw_input())
C = [map(int,raw_input().split()) for i in xrange(N)]
ans = 0
for i in xrange(N):
    for j in xrange(i+1,N):
        ans += min(C[i][j], C[j][i])
print ans