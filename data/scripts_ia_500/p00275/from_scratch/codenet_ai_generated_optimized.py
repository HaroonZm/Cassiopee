while True:
    N=int(input())
    if N==0:
        break
    c=input().strip()
    players=[0]*N
    field=0
    for i,ch in enumerate(c):
        p=i%N
        if ch=='M':
            players[p]+=1
        elif ch=='S':
            field+=players[p]+1
            players[p]=0
        else:
            players[p]+=field+1
            field=0
    print(*sorted(players),field)