from itertools import permutations

while True:
    a_ = [int(i) for i in input().split()]
    if a_ == [0, 0, 0, 0]:
        break
    perms = list(permutations(a_))
    found = False
    for a, b, c, d in perms:
        if found:
            break
        for i in ("+", "-", "*"):
            if found:
                break
            for j in ("+", "-", "*"):
                if found:
                    break
                for k in ("+", "-", "*"):
                    if found:
                        break
                    p = 0
                    exprs = [
                        ("({0}{4}{1}){5}{2}{6}{3}",    "(a{}b){}c{}d"),
                        ("({0}{4}{1}{5}{2}){6}{3}",     "(a{}b{}c){}d"),
                        ("{0}{4}({1}{5}{2}){6}{3}",     "a{}(b{}c){}d"),
                        ("{0}{4}({1}{5}{2}{6}{3})",     "a{}(b{}c{}d)"),
                        ("{0}{4}{1}{5}({2}{6}{3})",     "a{}b{}(c{}d)"),
                        ("(({0}{4}{1}){5}{2}){6}{3}",   "((a{}b){}c){}d"),
                        ("({0}{4}{1}){5}({2}{6}{3})",   "(a{}b){}(c{}d)"),
                        ("{0}{4}(({1}{5}{2}){6}{3})",   "a{}((b{}c){}d)"),
                        ("({0}{4}({1}{5}{2})){6}{3}",   "(a{}(b{}c)){}d"),
                        ("{0}{4}({1}{5}({2}{6}{3}))",   "a{}(b{}(c{}d))"),
                        ("{0}{4}{1}{5}{2}{6}{3}",       "a{}b{}c{}d")
                    ]
                    for fmt, form in exprs:
                        try:
                            p = eval(form.format(i, j, k))
                        except Exception:
                            continue
                        if p == 10:
                            print(fmt.format(a, b, c, d, i, j, k))
                            found = True
                            break
    if not found:
        print("0")