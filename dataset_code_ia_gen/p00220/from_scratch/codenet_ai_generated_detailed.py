def decimal_to_binary_limited(n):
    """
    Convert a decimal number to binary string with constraints:
    - Integer part: max 8 bits
    - Fractional part: max 4 bits
    If conversion does not fit in these constraints, return 'NA'.
    """
    # Split integer and fractional parts
    integer_part = int(n)
    fractional_part = abs(n - integer_part)

    # Convert integer part to binary without leading '0b'
    int_bin = bin(integer_part)[2:]

    # Check integer part length constraint
    if len(int_bin) > 8:
        return "NA"

    # Pad integer part to 8 bits with leading zeros
    int_bin = int_bin.zfill(8)

    # Convert fractional part to binary with 4 fractional bits max
    frac_bin = []
    frac = fractional_part
    for _ in range(4):
        frac *= 2
        bit = int(frac)
        frac_bin.append(str(bit))
        frac -= bit

    # Check if fractional part is exact within 4 bits: frac should be 0
    # If not, output 'NA'
    if frac > 0.0000001:  # small tolerance for floating-point imprecision
        return "NA"

    frac_bin_str = "".join(frac_bin)

    return int_bin + "." + frac_bin_str


def main():
    import sys

    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue

        # Parse input number as float
        try:
            n = float(line)
        except ValueError:
            # invalid input line, skip
            continue

        # Stop input on negative number
        if n < 0:
            break

        # Convert and print result
        result = decimal_to_binary_limited(n)
        print(result)


if __name__ == "__main__":
    main()