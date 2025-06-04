ON = True
f = lambda: int(input())
while ON:
    hds, c = [], 0
    z = f()
    if z == 0: ON ^= ON; continue
    hds += [z]
    exec('hds+=[f()];'*4)
    s = set(); [s.add(x) for x in hds]
    if not len(s)-2:
        a, b = sorted(list(s))
        for i in range(5):
            v = hds[i]==a
            print(abs((b==2)-(not a)+v*(2-(a==1)+(b==3 and a==1))))
    else:
        [print(3) for _ in hds]