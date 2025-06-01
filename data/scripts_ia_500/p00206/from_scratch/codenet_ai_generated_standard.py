while True:
    L = int(input())
    if L == 0:
        break
    savings = 0
    months = 0
    for i in range(12):
        M, N = map(int, input().split())
        savings += M - N
        if savings >= L and months == 0:
            months = i + 1
    print(months if months != 0 else "NA")