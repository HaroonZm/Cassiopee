def solve():
    M = 10 ** 6
    e = 10 ** 3
    
    # the sieve of Eratosthenes
    primes = [True] * (M + 1)
    primes[0] = False
    primes[1] = False
    for i in range(2, e):
        if primes[i]:
            for j in range(i * 2, M + 1, i):
                primes[j] = False
    
    # Create square grid sequence
    sg = [[None] * e for i in range(e)]
    for i, t_el, r1, r2 in zip(range(e // 2), range(e, 1, -2),sg, sg[::-1]):
        s1 = t_el ** 2
        s2 = s1 - 3 * (t_el) + 3
        
        r1[i:i+t_el] = range(s1, s1 - t_el, -1)
        r2[i:i+t_el] = range(s2, s2 + t_el)
    
    for i, t_el in zip(range(e // 2 - 1), range(e - 2, 1, -2)):
        s1 = t_el ** 2 + 1
        s2 = s1 + t_el * 3 + 1
        for c, n1, n2 in zip(sg[i+1:i+1+t_el], range(s1, s1 + t_el),
                             range(s2, s2 - t_el, -1)):
            c[i] = n1
            c[i+t_el+1] = n2
    
    from sys import stdin
    file_input = stdin
    
    while True:
        m, n = map(int, file_input.readline().split())
        if m == 0:
            break
        
        # calculate the position of n
        sn = n ** 0.5
        i_sn = int(sn)
        mid = e // 2
        h_i_sn = i_sn // 2
        if i_sn % 2:
            if sn == i_sn:
                s_r = mid + h_i_sn # start row
                s_c = s_r - 1 # start column
            elif n >= (i_sn ** 2) + i_sn + 1: # on the upper side
                s_r = mid - h_i_sn - 1
                s_c = mid - h_i_sn - 1 + (i_sn + 1) ** 2 - n
            else: # on the right side
                s_r = mid + h_i_sn - n + i_sn ** 2 + 1
                s_c = mid + h_i_sn
        else:
            if sn == i_sn:
                s_r = mid - h_i_sn
                s_c = s_r
            elif n <= (i_sn ** 2) + i_sn: # on the left side
                s_r = mid - h_i_sn + n - i_sn ** 2 - 1
                s_c = mid - h_i_sn - 1
            else: # on the lower side
                s_r = mid + h_i_sn
                s_c = mid + h_i_sn - 1 - (i_sn + 1) ** 2 + n
        
        # calculate the required square grid size
        sm = m ** 0.5
        i_sm = int(sm)
        h_i_sm = i_sm // 2
        if i_sm % 2:
            b = mid + h_i_sm # bottom
            l = mid - h_i_sm - 1 # leftmost
            if sm == i_sm:
                r = mid + h_i_sm - 1 # rightmost
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
        
        # optimize square grid
        t_sg = [x[l:r+1] for x in sg[s_r:b + 1]]
        
        c1 = s_c - l
        for i, x in zip(range(c1, 0, -1), t_sg):
            x[:i] = [0] * i
        c2 = r - s_c
        for i, x in zip(range(c2, 0, -1), t_sg):
            x[-i:] = [0] * i
            
        if t_sg[-1][0] == 0:
            for i, x in enumerate(t_sg[-1]):
                if x:
                    break
            t_sg = [x[i:] for x in t_sg]
        if t_sg[-1][-1] == 0:
            for i, x in enumerate(t_sg[-1][::-1]):
                if x:
                    break
            t_sg = [x[:-i] for x in t_sg]
        
        if m in t_sg[-1][1:]:
            x = t_sg[-1]
            i = x.index(m)
            x[i+1:] = [0] * (len(x) - i - 1)
        
        for x in t_sg:
            if x[0] > m:
                x[0] = 0
            if x[-1] > m:
                x[-1] = 0
        
        # DP
        rec_size = len(t_sg[0]) + 2
        prev = [0] * rec_size
        ans1 = 0
        ans2 = 0
        for x in t_sg:
            cur = [0] * rec_size
            for i, t in enumerate(zip(prev, prev[1:], prev[2:], x), start=1):
                a, b, c, y = t
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
            prev = cur
        
        print(ans1, ans2)
        

solve()