n=int(input())
ret = 0
for b in range(1,n):
    ret += (n-1)//b
print(ret)