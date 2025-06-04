from itertools import accumulate
n=int(input())
a=list(accumulate(map(int,input().split())))
for i in range(100,0,-1):
    for j in range(n):
        if i*(j+1)>a[j]:
            break
    else:
        print(i)
        break