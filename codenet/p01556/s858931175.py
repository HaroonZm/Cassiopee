def solve(lis,N):
    x=(lis[0][0]+lis[N//2][0])
    y=(lis[0][1]+lis[N//2][1])
    for i in range(1,N//2):
        if (lis[i][0]+lis[i+N//2][0])!=x or (lis[i][1]+lis[i+N//2][1])!=y:
            return "NA"
    return str(x/2)+" "+str(y/2)

N=int(input())
if N%2==1:
    print("NA")
else:
    lis=[]
    for i in range(N):
        lis.append(tuple(map(int,input().split())))
    ans=solve(lis,N)
    print(ans)