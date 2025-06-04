import sys

def to_float64_bits(e, frac):
    # Compose 64-bit string from exponent e and fraction frac
    return format(e, '012b') + format(frac, '052b')

def multiply_significand(frac, n):
    # frac: significand encoded as 52-bit int (without leading 1)
    # n: multiplier integer
    # returns (new_e, new_frac) in format:
    # number = (1 + frac/2^52) * n
    # output in form (e, frac) with 1 <= m < 2, m = 1 + frac/2^52
    total = (1 << 52) + frac
    total *= n  # integer multiplication
    e = total.bit_length() - 53  # shift to make 1 <= m < 2, subtract leading 1 bit
    if e < 0:
        # means total < 2^52, can't happen for n>=1 and original m>=1
        e = 0
    shift = e
    # truncate fraction bits after 52 bits by shifting right
    if shift > 0:
        frac_new = (total >> shift) & ((1 << 52) -1)
    else:
        frac_new = total & ((1 << 52) -1)
    return e, frac_new

def main():
    input = sys.stdin.read().split()
    i = 0
    while True:
        if i >= len(input):
            break
        nstr = input[i]
        i += 1
        if nstr == '0':
            break
        n = int(nstr)
        bits = input[i]
        i +=1
        frac = int(bits, 2)

        # initial a = m * 2^0, m = 1 + frac/(2^52)
        # sum s = n*a
        e, frac_res = multiply_significand(frac, n)
        # output bits: 12 bits exponent + 52 bits fraction
        print(to_float64_bits(e, frac_res))

if __name__ == '__main__':
    main()