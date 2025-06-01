x = []
for e in [[raw_input() for _ in [0] * 8] for _ in [0] * 3] + [x]:
    b = sorted(e, key=lambda x: x.split()[1])
    x += b[2:4]
    print '\n'.join(b[:2])