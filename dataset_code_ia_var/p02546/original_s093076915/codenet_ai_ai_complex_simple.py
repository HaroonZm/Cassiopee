from functools import reduce

s = input()
lmbd = lambda t: (lambda z: z[0] if z[1] else z[2])((t[0] + 'es', t[0][-1] == 's', t[0] + 's'))
print(lmbd((s,)))

# Variante avec itertools et mapping
# import itertools
# print(next(itertools.dropwhile(lambda x: not x[1], [(s+'es', s[-1]=='s'), (s+'s', True)]))[0])