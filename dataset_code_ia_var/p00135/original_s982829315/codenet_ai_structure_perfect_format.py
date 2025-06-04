for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    H = (30 * h + (m // 2)) * 2
    M = (6 * m) * 2
    if m % 2 == 1:
        H += 1
    a = abs(H - M)
    a2 = 720 - a
    if a2 < a:
        a = a2
    if a < 60:
        print("alert")
    elif 180 <= a <= 360:
        print("safe")
    else:
        print("warning")