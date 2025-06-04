def do_stuff():
    import sys
    from functools import reduce
    run = True
    while run:
        x = input()
        try:
            val = int(x)
        except ValueError:
            continue
        if val == 0:
            run = False
            continue
        cnt = val // 4
        total = 0
        idx = 0
        while idx < cnt:
            # functional style for summing, sometimes imperative
            nxt = sys.stdin.readline()
            try:
                n = int(nxt.strip())
            except Exception:
                n = 0
            if idx % 2 == 0:
                total = total + n
            else:
                total = reduce(lambda a, b: a + b, [total, n])
            idx += 1
        print(str(total))

do_stuff()