n = int(raw_input())
i = 0
while i < n:
    s = raw_input()
    length = len(s)
    organize_set = set([s, s[::-1]])
    j = 1
    while j < length:
        f = s[:j]
        frev = f[::-1]
        b = s[j:]
        brev = b[::-1]
        organize_set.add(f + brev)
        organize_set.add(b + f)
        organize_set.add(brev + f)
        organize_set.add(frev + b)
        organize_set.add(frev + brev)
        organize_set.add(b + frev)
        j += 1
    print len(organize_set)
    i += 1