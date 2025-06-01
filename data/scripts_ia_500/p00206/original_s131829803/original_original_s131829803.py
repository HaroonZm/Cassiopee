while True:
    v = int(input())
    if v == 0:
        break
    
    c = 0
    f = 0
    for i in range(1,13):
        m, n = [int(x) for x in input().split()]
        c += m - n
        if f == 0 and c >= v:
            f = i
    
    if f > 0:
        print(f)
    else:
        print("NA")