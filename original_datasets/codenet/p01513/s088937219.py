while True:
    n=int(input())
    if n==0:break
    mem=[]
    crime=-1
    for _ in range(n):
        mem.append(set([int(i) for i in input().split()][1:]))
    o=set([int(i) for i in input().split()][1:])
    for e,i in enumerate(mem):
        if o.intersection(i)==o:
            if crime==-1:crime=e+1
            else:
                crime=-1
                break
    print(crime)