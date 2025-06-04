L=int(input())
cats=list(map(int,input().split()))
stack=set()
inside=[]
for i,c in enumerate(cats,1):
    if c>0:
        if c in stack:
            print(i)
            break
        stack.add(c)
        inside.append(c)
    else:
        if -c not in stack:
            print(i)
            break
        if inside[-1]!=-c:
            print(i)
            break
        inside.pop()
        stack.remove(-c)
else:
    print("OK")