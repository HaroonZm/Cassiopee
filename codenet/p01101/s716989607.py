maxes=[]
cnt=0
while True:
    s=input()
    d=s.split()
    n=int(d[0])
    m=int(d[1])
    if n==0 and m==0:
        break

    s=input()
    d=s.split()
    a=[]
    
    for i in range(n):
        a.append(int(d[i]))

    p=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            p[i][j]=(a[i]+a[j])

    max=0
    for i in range(n):
        for j in range(i+1,n):
            if p[i][j]>m:
                continue
            if max<p[i][j]:
                max=p[i][j]
    if max==0:
        maxes.append(-1)
    else:
        maxes.append(max)
    cnt+=1

for i in range(cnt):
    if maxes[i]==-1:
        print("NONE")
    else:
        print(maxes[i])