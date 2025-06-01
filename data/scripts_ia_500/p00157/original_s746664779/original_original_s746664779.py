while True:
    n=int(input())
    if n==0:
        break
    dolls=[]
    for i in range(n):
        h,r=[int(j) for j in input().split(" ")]
        dolls.append((h,r))
    m=int(input())
    for j in range(m):
        h,r=[int(j) for j in input().split(" ")]
        dolls.append((h,r))

    dolls=sorted(dolls,key=lambda w:(w[0],-1*w[1]))
    r=[i[1] for i in dolls]

    table=[1 for i in range(len(r))]
    for i in range(len(r)):
        for j in range(i):
            if r[j]<r[i]:
                table[i]=max(table[i],table[j]+1)

    print(max(table))