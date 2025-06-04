import sys

prefixes = {
    "yotta": 24, "zetta": 21, "exa": 18, "peta": 15, "tera": 12,
    "giga": 9, "mega": 6, "kilo": 3, "hecto": 2, "deca": 1,
    "deci": -1, "centi": -2, "milli": -3, "micro": -6, "nano": -9,
    "pico": -12, "femto": -15, "ato": -18, "zepto": -21, "yocto": -24
}

def count_sigfigs(num_str):
    # Remove leading/trailing spaces
    s = num_str.strip()
    # Remove sign if any (problem states positive so no sign)
    # Remove decimal point for counting digits, keep track of decimal position for trailing zeros
    if '.' in s:
        left, right = s.split('.')
        left = left.lstrip('0')  # leading zeros before decimal not sig fig
        # trailing zeros after decimal ARE sig fig
        sigfig_str = left + right
        # if left is empty (all zeros), leading zeros in right removed as per rules 
        # but since problem states highest digit won't be zero except in 1's place, safe to consider as-is
        # just count all digits in sigfig_str
        if sigfig_str == '':
            # e.g. 0.0 etc, count zeros after decimal if any
            sigfig_str = '0'
        return len(sigfig_str)
    else:
        # integer form
        s = s.lstrip('0')
        if s == '':
            return 1  # number is zero
        # All digits count, including trailing zeros (per problem statement)
        return len(s)

def normalize(num_str):
    # returns (a_str, b_int)
    # num_str: e.g. "12.3", "0.000123", "1234.0"
    s = num_str
    if '.' in s:
        int_part, dec_part = s.split('.')
    else:
        int_part, dec_part = s, ''
    # remove leading zeros in int_part (but keep if number is zero)
    int_part = int_part.lstrip('0')
    if int_part:
        # exponent is length of int_part -1
        exp = len(int_part) - 1
        # significant digits: all int_part + dec_part
        digits = int_part + dec_part
        # first digit is digits[0]
        a = digits[0]
        if len(digits) > 1:
            a += '.' + digits[1:]
    else:
        # number < 1
        # count zeros after decimal before first nonzero digit
        count_zeros = 0
        for c in dec_part:
            if c == '0':
                count_zeros += 1
            else:
                break
        exp = - (count_zeros +1)
        # digits from first nonzero digit
        digits = dec_part[count_zeros:]
        a = digits[0]
        if len(digits) > 1:
            a += '.' + digits[1:]
    # remove trailing zeros after decimal in a only if they do not affect sig figs?
    # No, we must keep trailing zeros that are sig fig, so must keep all digits exactly as is for sig figs
    return a, exp

def round_to_sigfigs(a_str, sigfigs):
    # a_str in form like "1.234567"
    # we output to exactly sigfigs digits including before decimal
    # restore trailing zeros if needed
    if '.' not in a_str:
        # no decimal, just digits
        if len(a_str) == sigfigs:
            return a_str
        elif len(a_str) > sigfigs:
            # round digit
            digits = list(map(int, a_str))
            round_pos = sigfigs-1
            if digits[round_pos+1] >=5:
                digits[round_pos] +=1
            digits = digits[:sigfigs]
            # propagate carry
            for i in range(sigfigs-1,-1,-1):
                if digits[i] == 10:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0,1)
                    else:
                        digits[i-1] += 1
            return ''.join(str(x) for x in digits)
        else:
            # pad zeros to right
            return a_str + '0'*(sigfigs - len(a_str))
    else:
        int_part, dec_part = a_str.split('.')
        digits = int_part + dec_part
        if len(digits) == sigfigs:
            return a_str
        elif len(digits) > sigfigs:
            # round
            round_pos = sigfigs -1
            digits_list = list(map(int, digits))
            if digits_list[round_pos+1] >=5:
                digits_list[round_pos] +=1
            digits_list = digits_list[:sigfigs]
            # propagate carry
            for i in range(sigfigs-1,-1,-1):
                if digits_list[i] == 10:
                    digits_list[i] = 0
                    if i == 0:
                        digits_list.insert(0,1)
                    else:
                        digits_list[i-1] += 1
            # rebuild string with decimal point after len(int_part)
            new_int_len = len(int_part)
            if new_int_len >= len(digits_list):
                # all digits are int part
                int_new = ''.join(str(x) for x in digits_list) + '0'*(new_int_len - len(digits_list)) 
                return int_new
            else:
                int_new = ''.join(str(x) for x in digits_list[:new_int_len])
                dec_new = ''.join(str(x) for x in digits_list[new_int_len:])
                return int_new + '.' + dec_new
        else:
            # pad zeros to right
            needed = sigfigs - len(digits)
            dec_new = dec_part + '0'*needed
            return int_part + '.' + dec_new    

def process_line(line):
    parts = line.strip().split()
    if len(parts) == 2:
        num_str, unit = parts
        prefix = None
    else:
        num_str, prefix, unit = parts
    sigfigs = count_sigfigs(num_str)
    exp_offset = prefixes[prefix] if prefix else 0
    a, e = normalize(num_str)  # a in [1,10)
    # round a to sigfigs
    a_rounded = round_to_sigfigs(a, sigfigs)
    # adjust exponent if rounding changed leading digit count
    # check if a_rounded >=10
    if a_rounded[0] == '1' and a_rounded.startswith('10'):
        # occurs if rounding pushed over 10 (e.g. 9.99 -> 10.0)
        a_rounded = a_rounded[1:]  # drop leading 1 of "10", because 10 = 1 * 10^1
        e += 1
        a_rounded = a_rounded[0] + ('.' + a_rounded[1:] if len(a_rounded) > 1 else '')
    elif a_rounded.startswith('0'):
        # can occur if rounding zero? Problem states positive number so no zero
        pass
    print(f"{a_rounded} * 10^{e + exp_offset} {unit}")

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        line = input()
        process_line(line)

if __name__ == "__main__":
    main()