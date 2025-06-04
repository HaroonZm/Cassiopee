Q=int(input())
for _ in range(Q):
    n=input().strip()
    seen=set()
    count=0
    while len(n)>1:
        if n in seen:
            count=-1
            break
        seen.add(n)
        max_prod= -1
        for i in range(1,len(n)):
            a,b=n[:i], n[i:]
            prod=int(a)*int(b)
            if prod>max_prod:
                max_prod=prod
        n=str(max_prod)
        count+=1
    print(count)