n=int(input())
a=list(map(int,input().split()))[1:]
b=list(map(int,input().split()))[1:]
c=list(map(int,input().split()))[1:]
x=0
y=0
for i in range(1,n+1):
    if (i not in a) and (i not in b) and (i in c):
        x+=1
    elif (i in b) and (i in c):
        y+=1
print(x+y)