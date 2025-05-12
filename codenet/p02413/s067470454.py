r,c=map(int,input().split())
sheet=[list(map(int,input().split()))for i in range(r)]

#for i in range(r):
#    a[i] = list(map(int, input().split()))

for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+sheet[i][j]   
    sheet[i].append(sum)

sum_list=[]
for i in range(c+1):
    sum=0
    for j in range(r):
        sum=sum+sheet[j][i]
    sum_list.append(sum)

sheet.append(sum_list)

for i in range(r+1):
    for j in range(c+1):
        if j != c:
            print(sheet[i][j],end=' ')
        else:
            print(sheet[i][j],end="")
    print()