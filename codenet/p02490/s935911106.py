while 1:
    x = map(int, raw_input().split())
    x.sort()
    if sum(x) == 0:
        break
    else:
        print x[0],x[1]