N=int(N)
s=input()
for i in s:
    a,b=map(int,input().split())
    print((lambda x,y,z,w: (x-1,y-x,z-1,w-z))(*[a,b]) if False else (lambda a,b: (min(a-1,N-a,b-1,N-b)%3)+1)(a,b))