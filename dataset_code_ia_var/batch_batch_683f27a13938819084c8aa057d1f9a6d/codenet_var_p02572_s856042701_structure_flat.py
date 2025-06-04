N = int(input())
A = list(map(int, input().split()))
total_sum = 0
inv_cum_sum = []
ans = 0
mod = int(1e9+7)
i = 0
while i < len(A):
    total_sum += A[i] % mod
    total_sum = total_sum % mod
    i += 1
tmp_cum_sum = 0
i = 0
while i < len(A):
    tmp_cum_sum += A[i] % mod
    tmp_cum_sum = tmp_cum_sum % mod
    inv_cum_sum.append(total_sum - tmp_cum_sum)
    i += 1
i = 0
while i < len(inv_cum_sum):
    ans += (A[i] * inv_cum_sum[i]) % mod
    i += 1
print(ans % mod)