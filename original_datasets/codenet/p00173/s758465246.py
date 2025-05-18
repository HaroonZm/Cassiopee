list=[]
for i in range (9):
    n,a,b=input().split()
    a=int(a)
    b=int(b)
    list.append((n,a,b))
    print(n,a+b,a*200+b*300)