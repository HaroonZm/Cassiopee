while True:
    N, K = map(int, input().split())
    if N == 0:
        break
    S = [0]
    for x in input().split():
        S.append(int(x))
    flag = True
    for _ in range(N):
        B = []
        for x in input().split():
            B.append(int(x))
        i = 0
        while i < len(B):
            S[i+1] -= B[i]
            if S[i+1] < 0:
                flag = False
                break
            i += 1
        if not flag:
            # vider les entrées restantes
            for _ in range(_+1, N):
                input()
            break
    if flag:
        print("Yes")
    else:
        print("No")