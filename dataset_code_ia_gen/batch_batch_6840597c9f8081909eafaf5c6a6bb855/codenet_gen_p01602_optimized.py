n=int(input())
balance=0
for _ in range(n):
    p,x=input().split()
    x=int(x)
    if p=="(":
        balance+=x
    else:
        balance-=x
        if balance<0:
            print("NO")
            exit()
print("YES" if balance==0 else "NO")