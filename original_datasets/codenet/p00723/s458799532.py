def comp(sf, s1, s2):
    s = s1+s2
    if not(s in sf): sf.append(s)

m = int(raw_input())
for i in xrange(m):
    s = raw_input()
    c = ['', '']
    sf = []
    for j in xrange(1, len(s)):
        c = s[:j],s[j:]
        comp(sf, c[0], c[1])
        comp(sf, c[0], c[1][::-1])
        comp(sf, c[0][::-1], c[1])
        comp(sf, c[0][::-1], c[1][::-1])
        comp(sf, c[1], c[0])
        comp(sf, c[1], c[0][::-1])
        comp(sf, c[1][::-1], c[0])
        comp(sf, c[1][::-1], c[0][::-1])

    print len(sf)