import sys

while True:
    try:
        s = raw_input()
    except EOFError:
        break
    if s == '#':
        break
    angle = 0
    count = 0
    original_s = s
    while s:
        if count == 0:
            if s.endswith('north'):
                angle = 0
                s = s[:-5]
            elif s.endswith('west'):
                angle = 90
                s = s[:-4]
        else:
            if s.endswith('north'):
                angle -= 90.0 / (2 ** count)
                s = s[:-5]
            elif s.endswith('west'):
                angle += 90.0 / (2 ** count)
                s = s[:-4]
        count += 1
    denom = 1
    while angle != int(angle):
        angle *= 2
        denom *= 2
    if denom == 1:
        print int(angle)
    else:
        print "%d/%d" % (int(angle), denom)