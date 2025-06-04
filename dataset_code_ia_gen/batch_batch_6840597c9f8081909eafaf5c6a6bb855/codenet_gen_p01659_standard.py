n=int(input())
a=list(map(int,input().split()))
stack=[]
res=0
for h in a:
    count=1
    while stack and stack[-1][0]>=h:
        if stack[-1][0]==h:
            count+=stack[-1][1]
        else:
            res+=stack[-1][1]
        stack.pop()
    stack.append((h,count))
res+=sum(c for _,c in stack)
print(res)