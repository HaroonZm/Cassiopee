N,K = [int(i) for i in input().split()]

weight = 1
ans = 1
N -= 1

while N > 0:
    d = 0
    if weight % K == 0:
        d = weight // K
    else:
        d = weight // K + 1
    
    N -= d
    weight += d
    
    if N >= 0:
        ans += 1
        
print(ans)