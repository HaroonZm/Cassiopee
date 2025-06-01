def funk():
    q = True
    while q == True:
        r = [*input()]
        if "".join(r) == "0":
            q = False
            continue
        a = 0
        b = 0
        for x in r[1:]:
            a += (x == "A") * 1
            b += (x == "B") * 1
        (a, b) = (a + 1, b) if a > b else (a, b + 1)
        print(f"{a} {b}")

funk()