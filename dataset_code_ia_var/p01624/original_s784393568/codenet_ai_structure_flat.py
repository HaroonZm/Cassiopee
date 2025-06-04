ops = ["+", "*", "-", "&", "^", "|"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

while True:
    n, x = input().split(" ")
    n = int(n)
    if n == 0:
        quit()

    # get_nexts
    nexts = []
    # 削除
    for i in range(len(x)):
        y = x[:i] + x[i + 1:]

        # check
        op = 0
        bad = False
        for c in y:
            if c in ops:
                op += 1
                if op >= 2:
                    bad = True
                    break
            else:
                op = 0
        if bad:
            continue
        bad2 = False
        for opx in ops:
            if y.startswith(opx):
                bad2 = True
                break
            if ("(" + opx) in y:
                bad2 = True
                break
        if bad2:
            continue
        zero_ok = False
        bad3 = False
        for c in y:
            if not zero_ok and c == "0":
                bad3 = True
                break
            if c in numbers:
                zero_ok = True
            else:
                zero_ok = False
        if bad3:
            continue
        try:
            val = int(eval(y))
        except:
            continue
        nexts.append((val, y))

    # 追加
    for i in range(len(x) + 1):
        add_list = numbers + ops
        for s in add_list:
            y = x[:i] + s + x[i:]
            # check
            op = 0
            bad = False
            for c in y:
                if c in ops:
                    op += 1
                    if op >= 2:
                        bad = True
                        break
                else:
                    op = 0
            if bad:
                continue
            bad2 = False
            for opx in ops:
                if y.startswith(opx):
                    bad2 = True
                    break
                if ("(" + opx) in y:
                    bad2 = True
                    break
            if bad2:
                continue
            zero_ok = False
            bad3 = False
            for c in y:
                if not zero_ok and c == "0":
                    bad3 = True
                    break
                if c in numbers:
                    zero_ok = True
                else:
                    zero_ok = False
            if bad3:
                continue
            try:
                val = int(eval(y))
            except:
                continue
            nexts.append((val, y))

    if n % 2 == 1:
        nexts.sort(key=lambda a: -a[0])
        print(nexts[0][0])
        continue

    minvals = []
    for (val, y) in nexts:
        # get_nexts_val
        vals = []
        # 削除
        for j in range(len(y)):
            z = y[:j] + y[j + 1:]
            # check
            op = 0
            bad = False
            for c in z:
                if c in ops:
                    op += 1
                    if op >= 2:
                        bad = True
                        break
                else:
                    op = 0
            if bad:
                continue
            bad2 = False
            for opx in ops:
                if z.startswith(opx):
                    bad2 = True
                    break
                if ("(" + opx) in z:
                    bad2 = True
                    break
            if bad2:
                continue
            zero_ok = False
            bad3 = False
            for c in z:
                if not zero_ok and c == "0":
                    bad3 = True
                    break
                if c in numbers:
                    zero_ok = True
                else:
                    zero_ok = False
            if bad3:
                continue
            try:
                val2 = int(eval(z))
            except:
                continue
            vals.append(val2)
        # 追加
        for j in range(len(y) + 1):
            add_list = numbers + ops
            for s2 in add_list:
                z = y[:j] + s2 + y[j:]
                # check
                op = 0
                bad = False
                for c in z:
                    if c in ops:
                        op += 1
                        if op >= 2:
                            bad = True
                            break
                    else:
                        op = 0
                if bad:
                    continue
                bad2 = False
                for opx in ops:
                    if z.startswith(opx):
                        bad2 = True
                        break
                    if ("(" + opx) in z:
                        bad2 = True
                        break
                if bad2:
                    continue
                zero_ok = False
                bad3 = False
                for c in z:
                    if not zero_ok and c == "0":
                        bad3 = True
                        break
                    if c in numbers:
                        zero_ok = True
                    else:
                        zero_ok = False
                if bad3:
                    continue
                try:
                    val2 = int(eval(z))
                except:
                    continue
                vals.append(val2)
        vals.sort()
        minvals.append(vals[0])
    print(max(minvals))