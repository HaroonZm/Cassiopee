n, k = list(map(int, input().split()))

if k == 0:
    print(n**2)
    exit()
    
ans = 0
for b in range(k+1, n+1):
    ans_bk = (n-k)//b+1
    ans_b = ans_bk*(b-k)
    
    mod_k_max = ((n-k)//b)*b+k
    if n-mod_k_max+1 < b-k:
        ans_b -= ((b-k) - (n-mod_k_max+1))
    # print(ans_b)
    ans += ans_b
            
print(ans)