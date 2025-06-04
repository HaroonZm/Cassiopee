import sys

sys.setrecursionlimit(10000000)

N = input()
i = 0
while i < N:
    lst = []
    while len(lst) < 9:
        lst_ = raw_input().split()
        j = 0
        while j < len(lst_):
            lst.append(int(lst_[j], 16))
            j += 1
    res = lst[8]
    lst = lst[:8]
    diff = (sum(lst) - res) % (1 << 32)
    diff_lst = []
    k = 0
    while k < 32:
        D = 0
        l = 0
        while l < len(lst):
            if (lst[l] & (1 << k)) == 0:
                D += (1 << k)
            else:
                D -= (1 << k)
            l += 1
        if (res & (1 << k)) == 0:
            D -= (1 << k)
        else:
            D += (1 << k)
        D %= (1 << 32)
        diff_lst.append([D, 1 << k])
        k += 1
    L1 = [[diff, 0]]
    m = 0
    while m < 16:
        P = diff_lst[m]
        n = 0
        L = []
        while n < len(L1):
            L.append([(L1[n][0] + P[0]) % (1 << 32), L1[n][1] + P[1]])
            n += 1
        L1 += L
        m += 1
    L2 = [[0, 0]]
    o = 16
    while o < 32:
        P = diff_lst[o]
        n = 0
        L = []
        while n < len(L2):
            L.append([(L2[n][0] + P[0]) % (1 << 32), L2[n][1] + P[1]])
            n += 1
        L2 += L
        o += 1
    L1.sort()
    L2.sort()
    if L1[0][0] == 0:
        print hex(L1[0][1])[2:]
        i += 1
        continue
    pos = len(L2) - 1
    p = 0
    found = False
    while p < len(L1):
        while pos >= 0 and L1[p][0] + L2[pos][0] > (1 << 32):
            pos -= 1
        if pos >= 0 and L1[p][0] + L2[pos][0] == (1 << 32):
            print hex(L1[p][1] + L2[pos][1])[2:]
            found = True
            break
        p += 1
    i += 1