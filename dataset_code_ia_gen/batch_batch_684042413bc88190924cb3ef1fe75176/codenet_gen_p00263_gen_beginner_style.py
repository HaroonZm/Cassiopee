Q = int(input())
for _ in range(Q):
    s = input()
    n = int(s, 16)
    sign = (n >> 31) & 1
    int_val = 0
    for i in range(24):
        bit = (n >> (30 - i)) & 1
        int_val += bit * (1 << i)
    frac_val = 0.0
    for i in range(7):
        bit = (n >> (6 - i)) & 1
        frac_val += bit * (0.5 ** (i+1))
    val = int_val + frac_val
    if sign == 1:
        val = -val
    s_val = str(val)
    if '.' in s_val:
        s_val = s_val.rstrip('0').rstrip('.')
        if '.' not in s_val:
            s_val += '.0'
    else:
        s_val += '.0'
    print(s_val)