H,A=map(int,input().split())
HP=H
count=0
while HP>0:
    count+=1
    HP-=A
print(count)