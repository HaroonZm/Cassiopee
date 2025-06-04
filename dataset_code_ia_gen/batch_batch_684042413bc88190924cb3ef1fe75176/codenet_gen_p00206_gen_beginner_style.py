while True:
    L = input()
    if L == '0':
        break
    L = int(L)
    savings = 0
    month = 0
    reached = False
    for i in range(12):
        M, N = input().split()
        M = int(M)
        N = int(N)
        savings += (M - N)
        month += 1
        if savings >= L and not reached:
            print(month)
            reached = True
    if not reached:
        print("NA")