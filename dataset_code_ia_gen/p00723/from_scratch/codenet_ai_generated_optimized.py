m=int(input())
for _ in range(m):
    s=input()
    n=len(s)
    res=set()
    for i in range(1,n):
        a,b=s[:i],s[i:]
        a_rev,a_flip=a,a[::-1]
        b_rev,b_flip=b,b[::-1]
        res.add(a+b)
        res.add(a+b_rev)
        res.add(a_rev+b)
        res.add(a_rev+b_rev)
        res.add(b+a)
        res.add(b+a_rev)
        res.add(b_rev+a)
        res.add(b_rev+a_rev)
    print(len(res))