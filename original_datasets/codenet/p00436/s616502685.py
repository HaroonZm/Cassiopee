n=int(input())
s=[i for i in range(1,2*n+1)]
for _ in range(int(input())):
    a=int(input())
    if a:
        s=s[a:]+s[:a]
    else: 
        s=[s[i+n*j]for i in range(n) for j in[0,1]]
print(*s,sep='\n')