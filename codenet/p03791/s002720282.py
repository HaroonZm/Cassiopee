def mod_factorial(N, d):
    ans = 1
    for i in range(1,N+1):
        ans = (ans * i) % d
    return ans

d = 10**9 + 7
N = int(input())
list_co = list(map(int, input().split()))

ans = 1      
for i, x in enumerate(list_co):
    if x < 2*(i+1) -1: #(i+1) : robot number, x : coordinate of robot(i+1)
        ans *= (i+1)
        list_co.pop(i-1)
ans = (ans * mod_factorial(len(list_co),d)) % d
print(ans)