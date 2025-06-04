Q=int(input())
for _ in range(Q):
    c,a,n=map(int,input().split())
    teams=0
    # 3C teams
    teams+=c//3
    c%=3
    # 2C1A teams
    teams+=min(c//2,a)
    c-=2*min(c//2,a)
    a-=min(c//2,a)
    # CAN teams
    can_teams=min(c,a,n)
    teams+=can_teams
    print(teams)