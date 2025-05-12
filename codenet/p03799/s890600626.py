n,m =  map(int,input().split())
if n >= m//2:
    ans = min(n,m//2)
else:
    ans = n
    m -= 2*n
    ans += m//4
print(ans)