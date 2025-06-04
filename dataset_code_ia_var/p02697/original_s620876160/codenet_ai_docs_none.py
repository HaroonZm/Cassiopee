N, M = map(int, input().split())
if N % 2 == 1:
    for i in range(1, M + 1):
        print(i, N - i)
else:
    ANS = []
    for i in range(1, N // 4 + 1):
        ANS.append((i, N // 2 - i))
    for i in range(1, N // 4 + 1):
        ANS.append((N // 2 + i, N + 1 - i))
    check = 0
    for a, b in ANS:
        if a != b:
            print(a, b)
            check += 1
        if check == M:
            break