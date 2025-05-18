x,y,z = map(int,input().split())
n = x // (z + y)
c = 0
for i in range(1,n+1):
    if ( y + z ) * i + z <= x:
        c = i
    else:
        break
print(c)