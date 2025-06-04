m = int(raw_input())
for i in xrange(m):
    s = raw_input()
    sf = []
    for j in xrange(1, len(s)):
        c0 = s[:j]
        c1 = s[j:]
        pairs = [
            (c0, c1),
            (c0, c1[::-1]),
            (c0[::-1], c1),
            (c0[::-1], c1[::-1]),
            (c1, c0),
            (c1, c0[::-1]),
            (c1[::-1], c0),
            (c1[::-1], c0[::-1])
        ]
        for a, b in pairs:
            combined = a + b
            if not(combined in sf):
                sf.append(combined)
    print len(sf)