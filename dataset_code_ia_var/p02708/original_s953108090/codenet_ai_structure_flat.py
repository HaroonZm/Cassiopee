mod = 10**9 + 7
N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
ans = 0
i = K
while i <= N+1:
    max_value = (N * i - 2 * (((i-1)*i)//2)) % mod
    ans += max_value + 1
    i += 1
print(ans % mod)