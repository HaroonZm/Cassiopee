H,A,B=map(int,input().split())
count=0
for h in range(A,B+1):
    if H%h==0:
        count+=1
print(count)