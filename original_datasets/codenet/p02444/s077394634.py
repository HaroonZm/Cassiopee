n = int(input())
a = list(map(int,input().split()))
q = int(input())
for i in range(q):
    b,m,e = map(int,input().split())
    s = a[b:e]
    a = a[:b] + s[m-b:] + s[:m-b] + a[e:]
    
print(*a)