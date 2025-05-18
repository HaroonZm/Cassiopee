def cal(a,b):
    return a[0]*b[1]-a[1]*b[0]

c=1

while 1:
    N=int(input())
    if N==0:
        break
    p=[tuple(map(int, input().split())) for _ in range(N)]
    input()
    S=0
    for i in range(N):
        S += cal(p[i],p[i-1])
    S=abs(S/2)
    print("{} {}".format(c,S))
    c+=1