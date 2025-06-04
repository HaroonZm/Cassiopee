import sys
input=sys.stdin.readline

m=int(input())
for _ in range(m):
    initial_amount=int(input())
    years=int(input())
    n=int(input())
    max_final=0
    for __ in range(n):
        t,r,c=input().split()
        t=int(t)
        r=float(r)
        c=int(c)
        if t==1:
            balance=initial_amount
            for _ in range(years):
                interest=round(balance*r)
                balance=balance+interest-c
            final=balance
        else:
            balance=initial_amount
            cum_interest=0
            for _ in range(years):
                interest=round(balance*r)
                cum_interest+=interest
                balance=balance - c
            final=balance+cum_interest
        if final>max_final:
            max_final=final
    print(max_final)