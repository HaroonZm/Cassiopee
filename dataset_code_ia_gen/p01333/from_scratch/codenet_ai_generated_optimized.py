while True:
    A,B=map(int,input().split())
    if A==0 and B==0:
        break
    change=B-A
    n1000=change//1000
    change%=1000
    n500=change//500
    change%=500
    n100=change//100
    print(n100,n500,n1000)