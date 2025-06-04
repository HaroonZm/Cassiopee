while True:
    W_D = input().split()
    W = int(W_D[0])
    D = int(W_D[1])
    if W == 0 and D == 0:
        break
    hw_list = input().split()
    hd_list = input().split()
    hw = []
    for x in hw_list:
        hw.append(int(x))
    hd = []
    for x in hd_list:
        hd.append(int(x))
    total_hw = 0
    for num in hw:
        total_hw += num
    total_hd = 0
    for num in hd:
        total_hd += num
    # Find duplicates
    common = []
    for num in hw:
        if num in hd:
            common.append(num)
            hd.remove(num)
    sum_common = 0
    for num in common:
        sum_common += num
    print(total_hw + total_hd - sum_common)