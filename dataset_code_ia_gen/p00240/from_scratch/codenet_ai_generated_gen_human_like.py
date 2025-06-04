while True:
    n = int(input())
    if n == 0:
        break
    y = int(input())
    best_bank = None
    best_total = -1
    for _ in range(n):
        b, r, t = input().split()
        b = int(b)
        r = int(r)
        t = int(t)
        principal = 100
        if t == 1:
            # 単利
            total = principal + principal * r * y / 100
        else:
            # 複利
            total = principal * (1 + r / 100) ** y
        if total > best_total:
            best_total = total
            best_bank = b
    print(best_bank)