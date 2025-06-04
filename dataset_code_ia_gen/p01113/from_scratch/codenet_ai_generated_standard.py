import sys

def parse_significand(bits):
    return (1 << 52) + int(bits, 2)

def to_float64_bits(e, m):
    e_bits = format(e, '012b')
    m_bits = format(m & ((1 << 52) - 1), '052b')
    return e_bits + m_bits

def add_fp(e1, m1, e2, m2):
    # Align exponents
    if e1 > e2:
        shift = e1 - e2
        if shift > 52:
            # m2 becomes 0 effectively
            m2 = 0
        else:
            m2 >>= shift
        e = e1
        m = m1 + m2
    else:
        shift = e2 - e1
        if shift > 52:
            m1 = 0
        else:
            m1 >>= shift
        e = e2
        m = m1 + m2
    # Normalize
    if m >= (1 << 53):
        m >>= 1
        e += 1
    return e, m

def multiply_int_fp(n, e, m):
    # n is up to 10^18, use double-and-add method
    res_e = 0
    res_m = 0
    bit_pos = n.bit_length()
    cur_e, cur_m = e, m
    res_e, res_m = 0, 0
    first = True
    for i in reversed(range(bit_pos)):
        if not first:
            # Double res
            res_e, res_m = add_fp(res_e, res_m, res_e, res_m)
        else:
            first = False
        if (n >> i) & 1:
            if res_e == 0 and res_m == 0:
                res_e, res_m = cur_e, cur_m
            else:
                res_e, res_m = add_fp(res_e, res_m, cur_e, cur_m)
    return res_e, res_m

def main():
    input_lines = sys.stdin.read().splitlines()
    i = 0
    while True:
        if i >= len(input_lines):
            break
        n_line = input_lines[i].strip()
        if n_line == '0':
            break
        n = int(n_line)
        i += 1
        bits = input_lines[i].strip()
        i += 1
        # initial number a has exponent 0 and significand 1.b52...b1
        m = parse_significand(bits)  # 53-bit integer with implicit 1
        e = 0
        # multiply a by n, approximating each addition by truncation done by add_fp

        # Use repeated addition as above is too slow.
        # Use multiply_int_fp to compute s = n * a in fp with truncation

        # multiply_int_fp simulates adding a n times with truncation
        s_e, s_m = multiply_int_fp(n, e, m)

        print(to_float64_bits(s_e, s_m))

if __name__ == "__main__":
    main()