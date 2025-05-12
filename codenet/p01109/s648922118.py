try:
    while True:
        n = int(input())
        if n == 0:
            break
        ika = 0
        a = list(map(int,input().split()))
        m = sum(a) / n
        for j in a:
            if j <= m:
                ika += 1 
        print(ika)
except EOFError:
    pass