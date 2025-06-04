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
    i = 0
    while i < len(x):
        y = x[:i] + x[i + 1:]
        # check
        op_cnt = 0
        invalid = False
        for c in y:
            if c in ops:
                op_cnt += 1
                if op_cnt >= 2:
                    invalid = True
                    break
            else:
                op_cnt = 0
        if not invalid:
            for op in ops:
                if y.startswith(op) or ("(" + op) in y:
                    invalid = True
                    break
        if not invalid:
            zero_ok = False
            for c in y:
                if not zero_ok and c == "0":
                    invalid = True
                    break
                if c in ops:
                    zero_ok = False
                elif c in numbers:
                    zero_ok = True
                else:
                    zero_ok = False
        if not invalid:
            try:
                val = int(eval(y))
                nexts.append((val, y))
            except:
                pass
        i += 1
    # 追加
    i = 0
    while i < len(x) + 1:
        add_list = numbers + ops
        for s in add_list:
            y = x[:i] + s + x[i:]
            op_cnt = 0
            invalid = False
            for c in y:
                if c in ops:
                    op_cnt += 1
                    if op_cnt >= 2:
                        invalid = True
                        break
                else:
                    op_cnt = 0
            if not invalid:
                for op in ops:
                    if y.startswith(op) or ("(" + op) in y:
                        invalid = True
                        break
            if not invalid:
                zero_ok = False
                for c in y:
                    if not zero_ok and c == "0":
                        invalid = True
                        break
                    if c in ops:
                        zero_ok = False
                    elif c in numbers:
                        zero_ok = True
                    else:
                        zero_ok = False
            if not invalid:
                try:
                    val = int(eval(y))
                    nexts.append((val, y))
                except:
                    pass
        i += 1
    if n % 2 == 1:
        nexts.sort(key=lambda a: -a[0])
        print(nexts[0][0])
        continue
    minvals = []
    for (val, y) in nexts:
        # get_nexts(y)
        nextss = []
        j = 0
        while j < len(y):
            z = y[:j] + y[j + 1:]
            op_cnt = 0
            invalid = False
            for c in z:
                if c in ops:
                    op_cnt += 1
                    if op_cnt >= 2:
                        invalid = True
                        break
                else:
                    op_cnt = 0
            if not invalid:
                for op in ops:
                    if z.startswith(op) or ("(" + op) in z:
                        invalid = True
                        break
            if not invalid:
                zero_ok = False
                for c in z:
                    if not zero_ok and c == "0":
                        invalid = True
                        break
                    if c in ops:
                        zero_ok = False
                    elif c in numbers:
                        zero_ok = True
                    else:
                        zero_ok = False
            if not invalid:
                try:
                    vval = int(eval(z))
                    nextss.append((vval, z))
                except:
                    pass
            j += 1
        j = 0
        while j < len(y) + 1:
            add_list = numbers + ops
            for s in add_list:
                z = y[:j] + s + y[j:]
                op_cnt = 0
                invalid = False
                for c in z:
                    if c in ops:
                        op_cnt += 1
                        if op_cnt >= 2:
                            invalid = True
                            break
                    else:
                        op_cnt = 0
                if not invalid:
                    for op in ops:
                        if z.startswith(op) or ("(" + op) in z:
                            invalid = True
                            break
                if not invalid:
                    zero_ok = False
                    for c in z:
                        if not zero_ok and c == "0":
                            invalid = True
                            break
                        if c in ops:
                            zero_ok = False
                        elif c in numbers:
                            zero_ok = True
                        else:
                            zero_ok = False
                if not invalid:
                    try:
                        vval = int(eval(z))
                        nextss.append((vval, z))
                    except:
                        pass
            j += 1
        nextss.sort(key=lambda a: a[0])
        minvals.append(nextss[0][0])
    print(max(minvals))