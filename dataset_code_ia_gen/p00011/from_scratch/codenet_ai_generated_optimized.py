w=int(input())
n=int(input())
lines=list(range(1,w+1))
for _ in range(n):
 a,b=map(int,input().split(','))
 lines[a-1],lines[b-1]=lines[b-1],lines[a-1]
print('\n'.join(map(str,lines)))