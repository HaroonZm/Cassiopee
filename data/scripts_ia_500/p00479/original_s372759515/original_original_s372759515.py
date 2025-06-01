N=int(input())
for _ in[0]*int(input()):
 a,b=map(int,input().split())
 print(min(a-1,N-a,b-1,N-b)%3+1)