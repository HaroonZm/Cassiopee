h, w = map(int, raw_input().split(' '))
d = {}

def quat(l):
    a = 0
    for b in l:
        a += b % 4
    return a

def odd(l):
    a = 0
    for b in l:
        a += b % 2
    return a

for i in range(h):
    s = raw_input()
    for j in range(w):
        if s[j] in d:
            d[s[j]] += 1
        else:
            d[s[j]] = 1

l = []
for k in d:
    l.append(d[k])

if h * w % 2 == 1:
    if odd(l) != 1 or h + w - 1 < quat(l):
        print "No"
    else:
        print "Yes"
elif h % 2 == 1:
    if odd(l) != 0 or w < quat(l):
        print "No"
    else:
        print "Yes"
elif w % 2 == 1:
    if odd(l) != 0 or h < quat(l):
        print "No"
    else:
        print "Yes"
else:
    if quat(l) == 0:
        print "Yes"
    else:
        print "No"