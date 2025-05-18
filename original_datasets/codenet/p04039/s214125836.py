N, K = map(int, input().split())
D = set(map(str, input().split()))

while True:
    S = str(N)
    hit = True
    for s in S:
        if s in D:
            N += 1
            hit = False
            break
    if hit:
        print(N)
        exit()