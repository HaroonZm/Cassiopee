while True:
    n = input()
    if n == 0: break
    pb = None
    ans = 0
    for i in range(n):
        i, h, w = map(int, raw_input().split())
        bmi = w/((float(h)/100)**2)
        a = abs(22-bmi)
        if pb is None:
            pb = a
            ans = i
        elif pb is not None and a < pb:
            pb = a
            ans = i
    else:
        print ans