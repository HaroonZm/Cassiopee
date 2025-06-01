import sys
input=sys.stdin.readline

while True:
    n,h=map(int,input().split())
    if n==0 and h==0:
        break
    # Pour chaque direction, on va marquer les cubes "percés" dans des arrays booléens
    # "xy" : percé verticalement le long z (du haut ou bas)
    # "xz" : percé le long y
    # "yz" : percé le long x
    xhole = [[[False]*n for _ in range(n)] for _ in range(n)] 

    # Pour chaque direction, on mémorise dans des matrices booléennes les lignes de trous
    # Trous selon c=a,b coord, perçant tout le long axe restant
    # Marquons un tableau 3D global, mais on peut marquer directement

    # On crée trois matrices pour marquer, à l'envers, les trous sur les 3 directions:
    # Pour "xy a b": x=a, y=b => on perce tout z en (a,b,*)
    # Pour "xz a b": x=a, z=b => on perce tout y en (a,*,b)
    # Pour "yz a b": y=a, z=b => on perce tout x en (*,a,b)

    holes = [[[False]*n for _ in range(n)] for _ in range(n)]

    for _ in range(h):
        c,a,b=input().split()
        a=int(a)-1
        b=int(b)-1
        if c=='xy':
            for z in range(n):
                holes[a][b][z]=True
        elif c=='xz':
            for y in range(n):
                holes[a][y][b]=True
        else: # yz
            for x in range(n):
                holes[x][a][b]=True

    cnt=0
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if not holes[x][y][z]:
                    cnt+=1
    print(cnt)