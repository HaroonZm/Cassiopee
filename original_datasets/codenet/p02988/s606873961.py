n=int(input())
p=[int(a) for a in input().split()]
cnt=0

for i in range(n-2):
    a=sorted(p[i:i+3])
    if p[i+1]==a[1]:
        cnt+=1
        #print(i,p[i:i+3])

print(cnt)