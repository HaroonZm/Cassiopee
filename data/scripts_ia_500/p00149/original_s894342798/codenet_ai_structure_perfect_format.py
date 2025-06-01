al, ar, bl, br, cl, cr, dl, dr = 0, 0, 0, 0, 0, 0, 0, 0
while True:
    try:
        l, r = map(float, raw_input().split())
        if l >= 1.1:
            al += 1
        elif 0.6 <= l < 1.1:
            bl += 1
        elif 0.2 <= l < 0.6:
            cl += 1
        else:
            dl += 1
        if r >= 1.1:
            ar += 1
        elif 0.6 <= r < 1.1:
            br += 1
        elif 0.2 <= r < 0.6:
            cr += 1
        else:
            dr += 1
    except EOFError:
        break
print "{} {}\n{} {}\n{} {}\n{} {}".format(al, ar, bl, br, cl, cr, dl, dr)