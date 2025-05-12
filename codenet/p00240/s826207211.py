while True:
    max_p = 0
    x = 0
    n = int(input())
    if n == 0:
        break
    y = int(input())
    l = [list(map(int,input().split())) for i in range(n)]

    for i in range(n):

        if l[i][2] == 1:
            p = 1 + ( y * l[i][1]/100)
        else:
            p = (1 + l[i][1]/100) ** y

        if p > max_p:
            max_p = p
            x = l[i][0]

    print(x)