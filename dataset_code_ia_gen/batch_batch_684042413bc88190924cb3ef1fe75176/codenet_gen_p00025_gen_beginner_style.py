while True:
    try:
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
    except EOFError:
        break
    hit = 0
    blow = 0
    for i in range(4):
        if a[i] == b[i]:
            hit += 1
    for i in range(4):
        for j in range(4):
            if i != j and a[i] == b[j]:
                blow += 1
    print(hit, blow)