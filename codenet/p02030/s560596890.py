n,m=map(int,input().split())
a = list(map(int,input().split()))+[1000000001]
b = list(map(int,input().split()))+[1000000001]
andlis=[]
orlis=[]
cura=0
curb=0
for _ in range(n+m):
    if a[cura]>b[curb]:
        orlis.append(b[curb])
        curb+=1
    elif a[cura]==b[curb]:
        andlis.append(a[cura])
        cura+=1
    elif a[cura]<b[curb]:
        orlis.append(a[cura])
        cura+=1
print(len(andlis),len(orlis))
for i in andlis:
    print(i)
for i in orlis:
    print(i)