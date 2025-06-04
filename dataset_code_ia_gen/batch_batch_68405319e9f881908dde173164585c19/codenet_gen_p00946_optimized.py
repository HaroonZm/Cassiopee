import sys
input=sys.stdin.readline

n,m=map(int,input().split())
requests=[int(input()) for _ in range(m)]

pos=[0]*(n+1)
curr_pos=-(m+1)
for i in range(1,n+1):
    pos[i]=i+m

for i,e in enumerate(requests):
    pos[e]=m - i

result = sorted(range(1,n+1), key=lambda x: pos[x])
print('\n'.join(map(str,result)))