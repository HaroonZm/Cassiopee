N=int(input())
a=[*map(int,input().split())]
d=[]
for i in range(N-1):
    d.append([0]*21)
d[0][a[0]]=1
i=1
while i<N-1:
    for j in range(21):
        add = j + a[i]
        sub = j - a[i]
        val = 0
        if add < 21:
            val += d[i-1][add]
        if sub >= 0:
            val += d[i-1][sub]
        d[i][j] = val
    i+=1
print(d[-1][a[-1]])