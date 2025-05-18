while True:
    n = int(input())
    if n == 0:
        break
    bridges = []
    for _ in range(n):
        t, b = map(int, input().split())
        bridges.append((t, b))
    bridges.sort(key = lambda x: x[1])

    flag = True
    sumt = 0
    for t, b in bridges:
        sumt += t
        if sumt > b:
            flag = False
            break
    
    if flag:
        print('Yes')
    else:
        print('No')