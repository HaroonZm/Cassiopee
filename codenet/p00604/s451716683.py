while 1:
    try:n=int(input())
    except:break
    print(sum((n-i)*x for i,x in enumerate(sorted(list(map(int,input().split()))))))