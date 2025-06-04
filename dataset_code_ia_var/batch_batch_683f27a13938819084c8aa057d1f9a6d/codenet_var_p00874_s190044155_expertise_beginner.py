while True:
    W_D = input().split()
    W = int(W_D[0])
    D = int(W_D[1])
    if W == 0 and D == 0:
        break

    hw_input = input().split()
    hw = []
    for x in hw_input:
        hw.append(int(x))

    hd_input = input().split()
    hd = []
    for x in hd_input:
        hd.append(int(x))

    # Count occurrences in hw
    cnt_hw = {}
    for x in hw:
        if x in cnt_hw:
            cnt_hw[x] += 1
        else:
            cnt_hw[x] = 1

    # Count occurrences in hd
    cnt_hd = {}
    for x in hd:
        if x in cnt_hd:
            cnt_hd[x] += 1
        else:
            cnt_hd[x] = 1

    # Case 1: Use hw as base, complete with missing from hd
    total1 = sum(hw)
    for key in cnt_hd:
        if key in cnt_hw:
            missing = cnt_hd[key] - cnt_hw[key]
            if missing > 0:
                total1 += missing * key
        else:
            total1 += cnt_hd[key] * key

    # Case 2: Use hd as base, complete with missing from hw
    total2 = sum(hd)
    for key in cnt_hw:
        if key in cnt_hd:
            missing = cnt_hw[key] - cnt_hd[key]
            if missing > 0:
                total2 += missing * key
        else:
            total2 += cnt_hw[key] * key

    print(min(total1, total2))