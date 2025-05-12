while(True):
    n = int(input())
    if not n: break
    maxind = 0
    maxnum = 0
    for _ in range(n):
        a,b,c = map(int,input().split())
        if maxnum < b+c: maxind=a; maxnum=b+c
    print(maxind,maxnum)