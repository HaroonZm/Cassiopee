def inverse_mr_j(s): return s[-1] + s[:-1]
def inverse_miss_c(s): return s[1:] + s[0]
def inverse_mr_e(s):
    l = len(s)
    if l % 2 == 0:
        return s[l//2:] + s[:l//2]
    else:
        return s[l//2+1:] + s[l//2] + s[:l//2]
def inverse_mr_a(s): return s[::-1]
def inverse_dr_p(s):
    res = []
    for c in s:
        if c.isdigit():
            res.append('9' if c == '0' else str(int(c) - 1))
        else:
            res.append(c)
    return ''.join(res)
def inverse_mr_m(s):
    res = []
    for c in s:
        if c.isdigit():
            res.append('0' if c == '9' else str(int(c) + 1))
        else:
            res.append(c)
    return ''.join(res)

inv_funcs = {'J': inverse_mr_j, 'C': inverse_miss_c, 'E': inverse_mr_e,
             'A': inverse_mr_a, 'P': inverse_dr_p, 'M': inverse_mr_m}

n = int(input())
for _ in range(n):
    order = input().strip()
    msg = input().strip()
    for m in reversed(order):
        msg = inv_funcs[m](msg)
    print(msg)