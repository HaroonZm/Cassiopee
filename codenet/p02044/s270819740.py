while True:
    a,b = map(int,input().split())
    if a == b == 0:
        break
    h = b//a
    for c in list(map(int,input().split())):
        if c < h:
            b -= h-c
    print(b)