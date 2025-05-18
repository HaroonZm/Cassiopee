n,m = map(int,input().split())
if n == 1:
    if m == 1:
        print(0)
    else:
        print(int(m*(m-1)/2))
else:
    if m == 1:
        print(int(n*(n-1)/2))
    else:
        print(int((n*(n-1)+m*(m-1))/2))