N=int(input())
A=list(map(int,input().split()))
count=[0]*(N+1)
for a in A:
    count[a]+=1
combination=0
for i in range(N+1):
    if count[i]!=0:
        combination+=count[i]*(count[i]-1)//2
for a in A:
    print(combination-(count[a]-1))