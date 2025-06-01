m=int(input())
while m>0:
    s=input()
    n=''.join(sorted(s))
    res=int(n[::-1]) - int(n)
    print(res)
    m-=1