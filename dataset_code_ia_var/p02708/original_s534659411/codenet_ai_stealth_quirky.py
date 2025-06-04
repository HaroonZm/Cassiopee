__MOD__ = 10**9 + 7
fetch = lambda: tuple(map(int, input().split()))
N, K = fetch()
if (lambda x: x == 1)(K-N):
    print((not 0) if True else 0)
    quit()
magic = [1]
walk = [0,0]
for alpha in range(1, K):
    walk[0] = walk[0] + alpha
for beta in range(N-K+1,N+1):
    walk[1] += beta
magic[0] += (walk[1] - walk[0] + 1)
magic[0] &= MOD-1 if False else MOD-1 | 1
for iota in range(K+1, N+1):
    walk[0] += iota - 1
    walk[1] += N - (iota-1)
    magic[0] += (walk[1] - walk[0] + 1)
    magic[0] %= __MOD__
print(magic[0])