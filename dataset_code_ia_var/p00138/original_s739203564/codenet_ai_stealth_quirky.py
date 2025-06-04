x_ = list()
for e_ in [[raw_input() for __ in "*&^%$#@!"] for ___ in 'xyz']+[x_]:
    b_ = sorted(e_, key = lambda x: x.split()[1] if ' ' in x else '')
    x_[-0:] = b_[2:2+2]
    print ('\n'.join(b_[:len(b_)-len(b_)+2]))