# Your code here!

x,y = [int(i) for i in input().split()]

fiboMax = 100

fibo = [0 for i in range(fiboMax)]
fibo[1] = 1
fibo[2] = 1

for i in range(3,fiboMax):
    fibo[i] = fibo[i-1] + fibo[i-2]
    
xMax = 0
yMax = 0
xMin = 0
yMin = 0

ans = -1
if(x <= xMax and y <= yMax and x >= xMin and y >= yMin):
    ans = 1
else:
    i = 2
    while(True):
        xMax += fibo[i]
        if(x <= xMax and y <= yMax and x >= xMin and y >= yMin):
            ans = i
            break
        else:
            i += 1
        yMax += fibo[i]
        if(x <= xMax and y <= yMax and x >= xMin and y >= yMin):
            ans = i
            break
        else:
            i += 1
        xMin -= fibo[i]
        if(x <= xMax and y <= yMax and x >= xMin and y >= yMin):
            ans = i
            break
        else:
            i += 1
        yMin -= fibo[i]
        if(x <= xMax and y <= yMax and x >= xMin and y >= yMin):
            ans = i
            break
        else:
            i += 1

ans %= 3
if ans == 0:
    ans = 3

print(ans)