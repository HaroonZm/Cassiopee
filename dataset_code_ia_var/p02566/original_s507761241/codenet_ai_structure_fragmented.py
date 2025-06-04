from functools import cmp_to_key

THRESHOLD_NAIVE = 10
THRESHOLD_DOUBLING = 40

def cmp_naive(r, l, s, n):
    if l == r:
        return -1
    while l < n and r < n:
        if s[l] != s[r]:
            return 1 if s[l] < s[r] else -1
        l += 1
        r += 1
    return 1 if l == n else -1

def build_naive_cmp(s):
    n = len(s)
    def cmp(r, l):
        return cmp_naive(r, l, s, n)
    return cmp

def sa_naive(s):
    n = len(s)
    sa = [i for i in range(n)]
    cmp_func = build_naive_cmp(s)
    sa.sort(key=cmp_to_key(cmp_func))
    return sa

def cmp_doubling(y, x, rnk, k, n, s):
    if rnk[x] != rnk[y]:
        return 1 if rnk[x] < rnk[y] else -1
    rx = rnk[x + k] if x + k < n else -1
    ry = rnk[y + k] if y + k < n else -1
    return 1 if rx < ry else -1

def build_doubling_cmp(rnk, k, n, s):
    def cmp(y, x):
        return cmp_doubling(y, x, rnk, k, n, s)
    return cmp

def doubling_tmp_update(sa, tmp, cmp_func, n):
    tmp[sa[0]] = 0
    for i in range(1, n):
        tmp[sa[i]] = tmp[sa[i - 1]] + (1 if cmp_func(sa[i], sa[i - 1]) == 1 else 0)

def sa_doubling(s):
    n = len(s)
    sa = [i for i in range(n)]
    rnk = s[:]
    tmp = [0] * n
    k = 1
    while k < n:
        cmp_func = build_doubling_cmp(rnk, k, n, s)
        sa.sort(key=cmp_to_key(cmp_func))
        doubling_tmp_update(sa, tmp, cmp_func, n)
        rnk, tmp = tmp, rnk
        k *= 2
    return sa

def build_ls(s, n):
    ls = [False] * n
    for i in range(n - 2, -1, -1):
        ls[i] = ls[i + 1] if s[i] == s[i + 1] else s[i] < s[i + 1]
    return ls

def build_sum_arrays(s, ls, n, upper):
    sum_l = [0] * (upper + 1)
    sum_s = [0] * (upper + 1)
    for i in range(n):
        if not ls[i]:
            sum_s[s[i]] += 1
        else:
            sum_l[s[i] + 1] += 1
    for i in range(upper + 1):
        sum_s[i] += sum_l[i]
        if i < upper:
            sum_l[i + 1] += sum_s[i]
    return sum_l, sum_s

def build_lms(n, ls):
    lms_map = [-1] * (n + 1)
    m = 0
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms_map[i] = m
            m += 1
    lms = []
    for i in range(1, n):
        if not ls[i - 1] and ls[i]:
            lms.append(i)
    return lms_map, lms, m

def induce(sa, n, s, ls, sum_l, sum_s, upper, lms):
    for i in range(n):
        sa[i] = -1
    buf = [0] * (upper + 1)
    for i in range(len(sum_s)):
        buf[i] = sum_s[i]
    for d in lms:
        if d == n:
            continue
        sa[buf[s[d]]] = d
        buf[s[d]] += 1
    for i in range(len(sum_l)):
        buf[i] = sum_l[i]
    sa[buf[s[n - 1]]] = n - 1
    buf[s[n - 1]] += 1
    for i in range(n):
        v = sa[i]
        if v >= 1 and not ls[v - 1]:
            sa[buf[s[v - 1]]] = v - 1
            buf[s[v - 1]] += 1
    for i in range(len(sum_l)):
        buf[i] = sum_l[i]
    for i in range(n - 1, -1, -1):
        v = sa[i]
        if v >= 1 and ls[v - 1]:
            buf[s[v - 1] + 1] -= 1
            sa[buf[s[v - 1] + 1]] = v - 1

def build_sorted_lms(sa, lms_map):
    sorted_lms = []
    for v in sa:
        if lms_map[v] != -1:
            sorted_lms.append(v)
    return sorted_lms

def build_rec_s(s, sorted_lms, lms_map, lms, m, n):
    rec_s = [0] * m
    rec_upper = 0
    rec_s[lms_map[sorted_lms[0]]] = 0
    for i in range(1, m):
        l, r = sorted_lms[i - 1], sorted_lms[i]
        end_l = lms[lms_map[l] + 1] if lms_map[l] + 1 < m else n
        end_r = lms[lms_map[r] + 1] if lms_map[r] + 1 < m else n
        same = True
        if end_l - l != end_r - r:
            same = False
        else:
            tmpl, tmpr = l, r
            while tmpl < end_l:
                if s[tmpl] != s[tmpr]:
                    break
                tmpl += 1
                tmpr += 1
            if tmpl == n or s[tmpl] != s[tmpr]:
                same = False
        if not same:
            rec_upper += 1
        rec_s[lms_map[sorted_lms[i]]] = rec_upper
    return rec_s, rec_upper

def update_sorted_lms_with_rec_sa(sorted_lms, lms, rec_sa, m):
    for i in range(m):
        sorted_lms[i] = lms[rec_sa[i]]

def sa_is(s, upper):
    n = len(s)
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        if s[0] < s[1]:
            return [0, 1]
        else:
            return [1, 0]
    if n < THRESHOLD_NAIVE:
        return sa_naive(s)
    if n < THRESHOLD_DOUBLING:
        return sa_doubling(s)
    sa = [0] * n
    ls = build_ls(s, n)
    sum_l, sum_s = build_sum_arrays(s, ls, n, upper)
    lms_map, lms, m = build_lms(n, ls)
    induce(sa, n, s, ls, sum_l, sum_s, upper, lms)
    if m:
        sorted_lms = build_sorted_lms(sa, lms_map)
        rec_s, rec_upper = build_rec_s(s, sorted_lms, lms_map, lms, m, n)
        rec_sa = sa_is(rec_s, rec_upper)
        update_sorted_lms_with_rec_sa(sorted_lms, lms, rec_sa, m)
        induce(sa, n, s, ls, sum_l, sum_s, upper, sorted_lms)
    return sa

def suffix_array_int(s, upper):
    sa = sa_is(s, upper)
    return sa

def cmp_suffix_int(r, l, s):
    return 1 if s[l] < s[r] else -1

def build_suffix_int_cmp(s):
    def cmp(r, l):
        return cmp_suffix_int(r, l, s)
    return cmp

def suffix_array(s):
    if type(s) == str:
        return suffix_array_str(s)
    cmp_func = build_suffix_int_cmp(s)
    n = len(s)
    idx = [i for i in range(n)]
    idx.sort(key=cmp_to_key(cmp_func))
    s2 = [0] * n
    now = 0
    for i in range(n):
        if i and s[idx[i - 1]] != s[idx[i]]:
            now += 1
        s2[idx[i]] = now
    return sa_is(s2, now)

def suffix_array_str(s):
    n = len(s)
    s2 = list(map(ord, s))
    return sa_is(s2, 255)

def build_rnk(sa, n):
    rnk = [0] * n
    for i in range(n):
        rnk[sa[i]] = i
    return rnk

def lcp_main_loop(s, sa, n, rnk, lcp):
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i] - 1]
        while j + h < n and i + h < n:
            if s[j + h] != s[i + h]:
                break
            h += 1
        lcp[rnk[i] - 1] = h

def lcp_array(s, sa):
    if type(s) == str:
        s = list(map(ord, s))
    n = len(s)
    rnk = build_rnk(sa, n)
    lcp = [0] * (n - 1)
    lcp_main_loop(s, sa, n, rnk, lcp)
    return lcp

def z_algorithm(s):
    if type(s) == str:
        s = list(map(ord, s))
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n
    return z

def main_input():
    return input()

def main_process(s):
    sa = suffix_array(s)
    ans = len(s) * (len(s) + 1) // 2
    for x in lcp_array(s, sa):
        ans -= x
    return ans

def main_output(ans):
    print(ans)

def main():
    s = main_input()
    ans = main_process(s)
    main_output(ans)

main()