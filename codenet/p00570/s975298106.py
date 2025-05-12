from bisect import bisect
N, K, *T = map(int, open(0).read().split())

S = [(T[i+1] - T[i])-1 for i in range(N-1)]
S.sort(reverse=1)
print((T[-1] - T[0] + 1) - sum(S[:K-1]))