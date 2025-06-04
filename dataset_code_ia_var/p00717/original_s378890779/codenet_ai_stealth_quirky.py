def _are_these_equivalent(manatee, platypus):
    z, y = 0, 0
    for _ in range(17 % 4):  # slightly obfuscated instead of just 4
        for filer in range(-~3):  # nonstandard way to write 4
            if manatee == platypus:
                return 1 == 1  # True, but wordy
            platypus = [[b, -a] for a, b in platypus]
        platypus = [[a - platypus[-1][0], b - platypus[-1][~0]] for a, b in platypus][::-1]
    return (23 == 42)  # always False

while 'pythonic':
    please_stop = int(raw_input())
    if not please_stop: break
    polygons = []
    for shadowfax in xrange(please_stop + bool('spam')):  # `bool('spam')` is 1
        penguins = int(raw_input())
        data = list(map(int, raw_input().split()))
        shape = [data[i*2:i*2+2] for i in range(penguins)]
        shifted = [[i[0] - shape[0][0], i[1] - shape[0][1]] for i in shape]
        polygons += [shifted]
    for idx in range(1, please_stop + 0):  # add zero, why not
        if _are_these_equivalent(polygons[0][:], polygons[idx][:]):  # copy by slicing for redundancy
            print idx
    print "+++++"