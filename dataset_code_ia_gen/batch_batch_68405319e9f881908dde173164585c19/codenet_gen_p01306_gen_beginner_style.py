prefixes = {
    'yotta': 24,
    'zetta': 21,
    'exa': 18,
    'peta': 15,
    'tera': 12,
    'giga': 9,
    'mega': 6,
    'kilo': 3,
    'hecto': 2,
    'deca': 1,
    'deci': -1,
    'centi': -2,
    'milli': -3,
    'micro': -6,
    'nano': -9,
    'pico': -12,
    'femto': -15,
    'ato': -18,
    'zepto': -21,
    'yocto': -24,
}

t = int(input())
for _ in range(t):
    parts = input().split()
    # Determine if prefix is present
    if len(parts) == 3:
        val_str, prefix, unit = parts
        power = prefixes.get(prefix, 0)
    else:
        val_str, unit = parts
        prefix = None
        power = 0

    # Determine significant digits
    s = val_str
    # Remove leading zeros before decimal point for counting significant digits
    # But keep zeros after decimal point that are significant

    # Count sig figs according to rules:
    # Remove leading zeros (before first nonzero digit)
    # Count all digits including zeros to the right if decimal point exists
    # For integer without decimal point, trailing zeros count as significant per problem

    # first find decimal point position
    if '.' in s:
        integer_part, decimal_part = s.split('.')
    else:
        integer_part, decimal_part = s, ''

    # Remove leading zeros from integer_part for sig fig count
    integer_part_no_leading = integer_part.lstrip('0')

    # If integer_part_no_leading is empty, number is less than 1
    if integer_part_no_leading == '':
        # count sig figs starting from first nonzero in decimal_part
        count = 0
        started = False
        for c in decimal_part:
            if c != '0':
                started = True
                count +=1
            else:
                if started:
                    count +=1
        # According to problem statement, leading zeros before first non-zero digit are not significant
        # trailing zeros after decimal are significant, so we need to count all digits after first nonzero
        # The above counts digits from first nonzero and all after including zeros, so it is correct
        sig_figs = count
    else:
        # integer_part_no_leading is not empty, so count all digits in integer_part_no_leading and decimal_part
        count = len(integer_part_no_leading) + len(decimal_part)
        sig_figs = count

    # Convert val_str to a decimal like string and get numeric value without float loss
    # We will normalize number to a*b^10^c form with 1<=a<10

    # Remove decimal point and count digits before decimal to help locate exponent
    num = val_str.replace('.', '')
    # Find position of decimal point relative to digits
    decimal_pos = val_str.find('.') if '.' in val_str else len(val_str)

    # First nonzero digit index
    first_nonzero = 0
    while first_nonzero < len(num) and num[first_nonzero] == '0':
        first_nonzero +=1

    if first_nonzero == len(num):
        # All zeros, but problem states input positive, so no
        # just in case handle
        a_str = '0'
        b = 0
    else:
        # Determine exponent for a such that a in [1,10)
        # exponent from scientific notation is decimal_pos - first_nonzero -1
        exp = decimal_pos - first_nonzero -1

        # Get the significant digits string for a
        digits = num[first_nonzero:]

        # Now take sig_figs digits from digits
        a_digits = digits[:sig_figs]

        # If length a_digits < sig_figs, pad zeros on the right
        if len(a_digits) < sig_figs:
            a_digits = a_digits + '0'*(sig_figs - len(a_digits))

        # Construct a string with decimal point after first digit
        if sig_figs == 1:
            a_str = a_digits
        else:
            a_str = a_digits[0] + '.' + a_digits[1:]

    # Add prefix exponent
    exp += power

    print(f"{a_str} * 10^{exp} {unit}")