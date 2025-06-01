while True:
    n = int(input())
    if n == 0:
        break
    lst = []
    for i in range(n):
        line = input().split()
        numbers = []
        for num in line:
            numbers.append(int(num))
        lst.append(numbers)
    lp_lq_lr_lc = input().split()
    lp = int(lp_lq_lr_lc[0])
    lq = int(lp_lq_lr_lc[1])
    lr = int(lp_lq_lr_lc[2])
    lc = int(lp_lq_lr_lc[3])

    found = False
    for item in lst:
        s = item[0]
        p = item[1]
        q = item[2]
        r = item[3]
        if p <= lp and q <= lq and r <= lr and (4 * p + 9 * q + 4 * r) <= lc:
            print(s)
            found = True
    if not found:
        print("NA")