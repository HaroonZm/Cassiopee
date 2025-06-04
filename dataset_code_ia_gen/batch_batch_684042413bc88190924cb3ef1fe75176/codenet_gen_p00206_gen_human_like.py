while True:
    L = input()
    if L == '0':
        break
    L = int(L)
    savings = 0
    reached = False
    for month in range(1, 13):
        M, N = map(int, input().split())
        savings += (M - N)
        if not reached and savings >= L:
            print(month)
            reached = True
    if not reached:
        print("NA")