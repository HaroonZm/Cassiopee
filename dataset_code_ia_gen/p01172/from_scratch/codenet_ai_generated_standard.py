def recurring_fraction_length(x, y):
    remainder_pos = {}
    remainder = x % y
    pos = 0
    while remainder and remainder not in remainder_pos:
        remainder_pos[remainder] = pos
        remainder = (remainder * 10) % y
        pos += 1
    if remainder == 0:
        return pos, 0
    start = remainder_pos[remainder]
    length = pos - start
    return start, length

while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    a, b = recurring_fraction_length(x, y)
    print(a, b)