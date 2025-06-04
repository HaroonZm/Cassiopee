n = int(input())
a = list(map(int, input().split()))
ans = 0
a_sum = [a[0]]
i = 0
while i < n - 1:
    a_sum.append((a_sum[i] + a[i + 1]) % 1000000007)
    ans += a_sum[i] * (a[i + 1] % 1000000007)
    i += 1
print(ans % 1000000007)