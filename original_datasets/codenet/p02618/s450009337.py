import random
D = int(input())
c = list(map(int,input().split()))
s = [list(map(int,input().split())) for k in range(D)]

def score(t):
    ret = 0
    last = [0]*26
    for k in range(D):
        last[t[k]-1] = k+1
        ret += s[k][t[k]-1]
        for i in range(26):
            ret -= c[i]*(k+1-last[i])
    return ret

ans = [1+k%26 for k in range(365)]
prev = score(ans)
for i in range(1,26):
    temp = [1+k%26 for k in range(i,365+i)]
    ima = score(temp)
    if ima > prev:
        prev = ima
        ans = temp[::]
print(*ans,sep="\n")