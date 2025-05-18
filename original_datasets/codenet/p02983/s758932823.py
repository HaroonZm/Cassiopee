L, R = map(int, input().split())
mod = 2019
ans = 2019
for i in range(L,R+1) :
    for j in range(i+1,R+1) :
        temp = (i*j)%mod
        ans = min(ans, temp)
        if ans == 0 :
            print(0)
            exit()

print(ans)