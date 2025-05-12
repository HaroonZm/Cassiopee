H,W=[int(i) for i in input().split(" ")]

city=[]
for i in range(H):
    C=input()
    row=[]
    timer=-1000
    for c in C:
        if c=="c":
            timer=0
            row.append(timer)
        else:
            timer+=1
            row.append(timer)
    city.append(row)

for i in range(H):
    for j in range(W):
        if city[i][j]<0:
            city[i][j]="-1"
        else:
            city[i][j]=str(city[i][j])

for c in city:
    print(" ".join(c))