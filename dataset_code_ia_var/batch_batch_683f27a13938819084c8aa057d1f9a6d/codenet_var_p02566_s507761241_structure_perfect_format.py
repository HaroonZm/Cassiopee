from functools import cmp_to_key

THRESHOLD_NAIVE = 10
THRESHOLD_DOUBLING = 40

def sa_naive(s):
    def cmp(r, l):
        if l == r:
            return -1
        while l < n and r < n:
            if s[l] != s[r]:
                return 1 if s[l] < s[r] else -1
            l += 1
            r += 1
        return 1 if l == n else -1
    n = len(s)
    sa = [i for i in range(n)]
    sa.sort(key=cmp_to_key(cmp))
    return sa

def sa_doubling(s):
    n = len(s)
    sa = [i for i in range(n)]
    rnk = s
    tmp = [0] * n
    k = 1
    while k < n:
        def cmp(y, x):
            if rnk[x] != rnk[y]:
                return 1 if rnk[x] < rnk[y] else -1
            rx = rnk[x + k] if x + k < n else -1
            ry = rnk[y + k] if y + k < n else -1
            return 1 if rx < ry else -1
        sa.sort(key=cmp_to_key(cmp))
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (1 if cmp(sa[i], sa[i - 1]) == 1 else 0)
        tmp, rnk = rnk, tmp
        k <<= 1
    return sa

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
    ls = [False] * n
    for i in range(n - 2, -1, -1):
        if s[i] == s[i + 1]:
            ls[i] = ls[i + 1]
        else:
            ls[i] = s[i] < s[i + 1]
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

    def induce(lms):
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

    induce(lms)

    if m:
        sorted_lms = []
        for v in sa:
            if lms_map[v] != -1:
                sorted_lms.append(v)
        rec_s = [0] * m
        rec_upper = 0
        rec_s[lms_map[sorted_lms[0]]] = 0
        for i in range(1, m):
            l = sorted_lms[i - 1]
            r = sorted_lms[i]
            end_l = lms[lms_map[l] + 1] if lms_map[l] + 1 < m else n
            end_r = lms[lms_map[r] + 1] if lms_map[r] + 1 < m else n
            same = True
            if end_l - l != end_r - r:
                same = False
            else:
                ll = l
                rr = r
                while ll < end_l:
                    if s[ll] != s[rr]:
                        break
                    ll += 1
                    rr += 1
                if ll == n or s[ll] != s[rr]:
                    same = False
            if not same:
                rec_upper += 1
            rec_s[lms_map[sorted_lms[i]]] = rec_upper
        rec_sa = sa_is(rec_s, rec_upper)
        for i in range(m):
            sorted_lms[i] = lms[rec_sa[i]]
        induce(sorted_lms)
    return sa

def suffix_array_upper(s, upper):
    sa = sa_is(s, upper)
    return sa

def suffix_array(s):
    if isinstance(s, str):
        return suffix_array_str(s)
    def cmp(r, l):
        return 1 if s[l] < s[r] else -1
    n = len(s)
    idx = [i for i in range(n)]
    idx.sort(key=cmp_to_key(cmp))
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

def lcp_array(s, sa):
    if isinstance(s, str):
        s = list(map(ord, s))
    n = len(s)
    rnk = [0] * n
    for i in range(n):
        rnk[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if h > 0:
            h -= 1
        if rnk[i] == 0:
            continue
        j = sa[rnk[i] - 1]
        while j + h < n and i + h < n and s[j + h] == s[i + h]:
            h += 1
        lcp[rnk[i] - 1] = h
    return lcp

def z_algorithm(s):
    if isinstance(s, str):
        s = list(map(ord, s))
    n = len(s)
    if n == 0:
        return []
    z = [0] * n
    j = 0
    for i in range(1, n):
        if j + z[j] <= i:
            z[i] = 0
        else:
            z[i] = min(j + z[j] - i, z[i - j])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n
    return z

s = input()
sa = suffix_array(s)
ans = len(s) * (len(s) + 1) // 2
for x in lcp_array(s, sa):
    ans -= x
print(ans)