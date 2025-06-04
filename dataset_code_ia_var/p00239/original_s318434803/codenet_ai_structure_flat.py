while True:
    n = int(input())
    if n == 0:
        break
    lst = []
    i = 0
    while i < n:
        lst.append(list(map(int, input().split())))
        i += 1
    temp = input().split()
    lp = int(temp[0])
    lq = int(temp[1])
    lr = int(temp[2])
    lc = int(temp[3])
    flag = True
    j = 0
    while j < len(lst):
        s = lst[j][0]
        p = lst[j][1]
        q = lst[j][2]
        r = lst[j][3]
        if p <= lp and q <= lq and r <= lr and 4 * p + 9 * q + 4 * r <= lc:
            print(s)
            flag = False
        j += 1
    if flag:
        print("NA")