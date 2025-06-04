N,K=map(int,input().split())
a=list(map(int,input().split()))
to_pick=N-K
stack=[]
for x in a:
    while stack and K>0 and stack[-1]<x:
        stack.pop()
        K-=1
    stack.append(x)
print(''.join(map(str,stack[:to_pick])))