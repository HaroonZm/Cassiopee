while True:
    n = int(input())
    if n == 0:
        break
    A_score = 0
    B_score = 0
    for _ in range(n):
        a, b = map(int, input().split())
        if a > b:
            A_score += a + b
        elif a < b:
            B_score += a + b
        else:
            A_score += a
            B_score += b
    print(A_score, B_score)