n = int(input())
print('0:')
for x in range(1, 2**n):
    bits = []
    y = x
    pos = 0
    while y > 0:
        if y & 1:
            bits.append(pos)
        y >>= 1
        pos += 1
    print(str(x) + ':', end='')
    for b in bits:
        print(' ' + str(b), end='')
    print()