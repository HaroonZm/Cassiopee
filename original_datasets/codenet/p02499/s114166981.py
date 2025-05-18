from string import lowercase as L
d={c:0 for c in L}
while True:
    try:
        s = raw_input()
    except:
        break
    for c in s.lower():
        if c in L:
            d[c] += 1
for c in L:
    print c, ':', d[c]