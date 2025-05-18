n = int(input())
a = list(map(int,input().split()))
ans = 0
keisu = [0]*n
t = 0

for i in range(n):
    
    keisu[i] += t
    t += a[i]

for i in range(n):
    ans += a[i] * keisu[i]

        
        

print(ans%(1000000000+7))