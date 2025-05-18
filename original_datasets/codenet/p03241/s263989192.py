def abc112_d():
    N, M = map(int, input().split())

    def divisor(n):
        ''' nの約数列挙 '''
        arr = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                arr.append(i)
                arr.append(n // i)
        return arr  # 戻り値はsortされていない

    ans = 1
    for d in divisor(M):
        if M // d >= N:
            ans = max(d, ans)
    print(ans)

abc112_d()