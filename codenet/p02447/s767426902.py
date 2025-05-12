n=int(input())
s=[]
for i in range(n):
    x,y=map(int,input().split())
    s.append((x,y))
s.sort()
for i in range(n):
    print(s[i][0],s[i][1])