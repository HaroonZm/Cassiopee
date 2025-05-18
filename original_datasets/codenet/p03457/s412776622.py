n = int(input())
t = [0] * (n+1)
x = [0] * (n+1)
y = [0] * (n+1)
for i in range(1,n+1):
    t[i],x[i],y[i] = map(int,input().split())

for i in range(n):
    tmp = abs(t[i+1]-t[i]) - (abs(x[i+1]-x[i]) + abs(y[i+1]-y[i]))
    if tmp < 0 or tmp % 2 != 0:    
        print('No')
        quit()
print('Yes')