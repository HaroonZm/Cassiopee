import math
n=int(input())
shop=input()
s=[input() for _ in range(n)]
m=len(shop)
cnt=[0]*n
for i in range(n):
    for j in range(len(s[i])):
        for k in range(1,2*math.ceil(len(s[i])/m)):
            if shop in s[i][j::k]:
                cnt[i]=1
print(sum(cnt))