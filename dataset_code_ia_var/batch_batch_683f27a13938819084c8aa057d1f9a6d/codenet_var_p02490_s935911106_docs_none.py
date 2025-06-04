while True:
    x = list(map(int, input().split()))
    x.sort()
    if sum(x) == 0:
        break
    else:
        print(x[0], x[1])