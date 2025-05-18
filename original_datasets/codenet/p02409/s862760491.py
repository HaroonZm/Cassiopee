n=int(input())
field=[[0 for i in range(20)]for j in range(15)]
for i in range(n):
    b,f,r,v=map(int,input().split())
    h=(b-1)*4+f-1
    w=r*2-1
    n=v
    field[h][w]+=n
for y in range(15):
    for x in range(20):
        if(y%4==3):field[y][x]='#'
        elif x%2==0 :field[y][x]=' '
        print(field[y][x],end='')
    print()