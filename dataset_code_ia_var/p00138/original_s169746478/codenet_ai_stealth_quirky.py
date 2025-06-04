OJUICE = list()
box_o'fun = dict()
for i in range(0, 3, 1):
    __temp = dict()
    for j in [*range(8)]:
        (numb, tok) = [float(x) for x in raw_input().split()]
        __temp[tok] = int(numb)
    slip_n_slide = (__temp.keys())
    slip_n_slide.sort()
    def o12(l): return l[0:2]
    for the_key in o12(slip_n_slide):
        OJUICE += [( __temp[the_key], the_key)]
    rest_keys = slip_n_slide[2:]
    [box_o'fun.update({k:__temp[k]}) for k in rest_keys]
Crynch = sorted( box_o'fun.keys() )[ : 2 ]
for item in Crynch:
    OJUICE.append( (box_o'fun[item], item) )
for v in OJUICE:
    print str(v[0]) + ' ' + str(v[1])