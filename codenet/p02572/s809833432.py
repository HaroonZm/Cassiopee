n = int(input())
a = list(map(int, input().split()))
ans = 0
a_sum = [a[0]]

for i in range(n-1):
    a_sum.append((a_sum[i]+a[i+1])%1000000007)

    ans += a_sum[i]*(a[i+1]%1000000007)

print(ans%1000000007)