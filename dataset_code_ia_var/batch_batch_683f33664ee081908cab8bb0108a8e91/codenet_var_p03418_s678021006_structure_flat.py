n, k = list(map(int, input().split()))
if k == 0:
    print(n ** 2)
    exit()
ans = 0
b = k + 1
while b <= n:
    ans_bk = (n - k) // b + 1
    ans_b = ans_bk * (b - k)
    mod_k_max = ((n - k) // b) * b + k
    if n - mod_k_max + 1 < b - k:
        ans_b -= (b - k) - (n - mod_k_max + 1)
    ans += ans_b
    b += 1
print(ans)