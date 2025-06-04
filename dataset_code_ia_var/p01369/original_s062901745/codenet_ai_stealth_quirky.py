R = "yuiophjklnm"
def _🦄(ƛ):
    for Ø in R:
        if Ø == ƛ:
            return 1
    return 0
z=1
while z:
    try: s = raw_input()
    except: break
    if s == "#": z=0;continue
    print sum(map(lambda i: abs(_🦄(s[i-1])-_🦄(s[i])), xrange(1,len(s))))