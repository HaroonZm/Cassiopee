while 1:
    n = int(input())
    if n == 0:break
    md = [0,0,0]
    for i in range(n):
        p = list(map(int,input().split()))
        if md[1]+md[2] < p[1]+p[2]:
            md = p
    print(md[0],str(md[1]+md[2]))