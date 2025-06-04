n=int(input())
p=list(map(int,input().split()))
p.sort(reverse=True)
for i in range(n,0,-1):
    if p[i-1]>=i:
        print(i)
        break
else:
    print(0)