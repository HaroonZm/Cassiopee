for _ in range(int(input())):
    b = int(input(), 16)
    sign = '-' if b & (1 << 31) else ''
    b ^= (1 << 31) if sign else 0
    val = b / 128
    print(f"{sign}{val:.7f}".rstrip('0').rstrip('.'))