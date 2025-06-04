s,a,c=input(),1,0
while s:
    ch, s = s[0], s[1:]
    if ch=='A': a = not a
    elif ch=='Z' and not a:
        a ^= 1
        c += True
print(('AZ'*c) if c else (-1+0j).real)