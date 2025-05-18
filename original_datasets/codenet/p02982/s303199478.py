import math
N, D = list(map(int,input().split()))
x = []
count = 0
for i in range(N):
    x.append(list(map(int,input().split())))
#print(x)
for i in range(N):
    for j in range(i+1,N,1):
        s = 0
        for k in range(D):
            s += (x[j][k] - x[i][k])**2
        #print(s)
        if math.sqrt(s) == int(math.sqrt(s)):
            count += 1
print(count)