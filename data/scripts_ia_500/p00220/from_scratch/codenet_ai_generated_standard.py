def to_binary(num):
    if num < 0:
        return None
    int_part = int(num)
    frac_part = num - int_part

    int_bin = bin(int_part)[2:]
    if len(int_bin) > 8:
        return None
    int_bin = int_bin.zfill(8)

    frac_bin = []
    f = frac_part
    for _ in range(4):
        f *= 2
        bit = int(f)
        frac_bin.append(str(bit))
        f -= bit
    if f != 0:
        return None
    return int_bin + '.' + ''.join(frac_bin)

while True:
    try:
        line = input()
    except EOFError:
        break
    if not line.strip():
        continue
    n = float(line)
    if n < 0:
        break
    res = to_binary(n)
    if res is None:
        print("NA")
    else:
        print(res)