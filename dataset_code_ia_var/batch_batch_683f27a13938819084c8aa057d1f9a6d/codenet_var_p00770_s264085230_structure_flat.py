M = 10 ** 6
e = 10 ** 3

# Crible d'Ératosthène
primes = [True] * (M + 1)
primes[0] = False
primes[1] = False
i = 2
while i < e:
    if primes[i]:
        j = i * 2
        while j <= M:
            primes[j] = False
            j += i
    i += 1

# Génération du carré spiralé
sg = []
i = 0
while i < e:
    sg.append([None] * e)
    i += 1

i = 0
while i < (e // 2):
    t_el = e - 2 * i
    s1 = t_el ** 2
    s2 = s1 - 3 * t_el + 3
    r1 = sg[i]
    r2 = sg[e - i - 1]
    r = 0
    v = s1
    while r < t_el:
        r1[i + r] = v
        v -= 1
        r += 1
    r = 0
    v = s2
    while r < t_el:
        r2[i + r] = v
        v += 1
        r += 1
    i += 1

i = 0
while i < (e // 2 - 1):
    t_el = e - 2 * (i + 1)
    s1 = t_el ** 2 + 1
    s2 = s1 + t_el * 3 + 1
    c_idx = 0
    while c_idx < t_el:
        c = sg[i + 1 + c_idx]
        n1 = s1 + c_idx
        n2 = s2 - c_idx
        c[i + 1] = n1
        c[i + t_el + 1] = n2
        c_idx += 1
    i += 1

import sys
file_input = sys.stdin

while True:
    line = ''
    while line.strip() == '':
        line = file_input.readline()
        if not line:
            break
    if not line:
        break
    m_n = line.strip().split()
    if not m_n:
        continue
    m, n = map(int, m_n)
    if m == 0:
        break

    sn = n ** 0.5
    i_sn = int(sn)
    mid = e // 2
    h_i_sn = i_sn // 2
    if i_sn % 2:
        if sn == i_sn:
            s_r = mid + h_i_sn
            s_c = s_r - 1
        elif n >= (i_sn ** 2) + i_sn + 1:
            s_r = mid - h_i_sn - 1
            s_c = mid - h_i_sn - 1 + (i_sn + 1) ** 2 - n
        else:
            s_r = mid + h_i_sn - n + i_sn ** 2 + 1
            s_c = mid + h_i_sn
    else:
        if sn == i_sn:
            s_r = mid - h_i_sn
            s_c = s_r
        elif n <= (i_sn ** 2) + i_sn:
            s_r = mid - h_i_sn + n - i_sn ** 2 - 1
            s_c = mid - h_i_sn - 1
        else:
            s_r = mid + h_i_sn
            s_c = mid + h_i_sn - 1 - (i_sn + 1) ** 2 + n

    sm = m ** 0.5
    i_sm = int(sm)
    h_i_sm = i_sm // 2
    if i_sm % 2:
        b = mid + h_i_sm
        l = mid - h_i_sm - 1
        if sm == i_sm:
            r = mid + h_i_sm - 1
        else:
            r = mid + h_i_sm
    else:
        r = mid + h_i_sm - 1
        if sm == i_sm:
            l = mid - h_i_sm
        else:
            l = mid - h_i_sm - 1
        if m <= i_sm ** 2 + i_sm:
            b = mid + h_i_sm - 1
        else:
            b = mid + h_i_sm

    t_sg = []
    idx = s_r
    while idx <= b:
        t_sg.append(sg[idx][l:r+1])
        idx += 1

    c1 = s_c - l
    i = 0
    while i < c1:
        t_sg[i][:c1 - i] = [0] * (c1 - i)
        i += 1
    c2 = r - s_c
    i = 0
    while i < c2:
        t_sg[i][:] = t_sg[i][:]
        t_sg[i][- (c2 - i):] = [0] * (c2 - i)
        i += 1

    if t_sg[-1][0] == 0:
        i = 0
        while i < len(t_sg[-1]):
            if t_sg[-1][i]:
                break
            i += 1
        t_sg = [x[i:] for x in t_sg]
    if t_sg[-1][-1] == 0:
        i = 0
        while i < len(t_sg[-1]):
            if t_sg[-1][-(i+1)]:
                break
            i += 1
        if i:
            t_sg = [x[: -i] for x in t_sg]

    if m in t_sg[-1][1:]:
        x = t_sg[-1]
        idx = x.index(m)
        x[idx + 1:] = [0] * (len(x) - idx - 1)

    for x in t_sg:
        if x[0] > m:
            x[0] = 0
        if x[-1] > m:
            x[-1] = 0

    rec_size = len(t_sg[0]) + 2
    prev = [0] * rec_size
    ans1 = 0
    ans2 = 0
    for x in t_sg:
        cur = [0] * rec_size
        i = 1
        while i < rec_size - 1:
            y = x[i - 1]
            a = prev[i - 1]
            b = prev[i]
            c = prev[i + 1]
            if primes[y]:
                v = 1 + max(a, b, c)
                if v == ans1 and y > ans2:
                    ans2 = y
                elif v > ans1:
                    ans1 = v
                    ans2 = y
            else:
                v = max(a, b, c)
            cur[i] = v
            i += 1
        prev = cur

    print(ans1, ans2)