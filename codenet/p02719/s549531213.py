N,K = list(map(int, input().split()))

a = int(N/K)
b = N % K
c = abs(b-K)

print(min(b,c))