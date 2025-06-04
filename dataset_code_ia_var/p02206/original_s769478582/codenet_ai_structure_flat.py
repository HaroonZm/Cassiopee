N, K = map(int, input().split())
OK = 0
NG = K + 1
while NG - OK > 1:
    mid = (OK + NG) // 2
    ANS = 0
    money = mid
    i = 0
    while i < N:
        ANS += money
        money //= 2
        if money == 0:
            break
        i += 1
    if ANS <= K:
        OK = mid
    else:
        NG = mid
print(OK)