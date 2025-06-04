# (!) Ce code reflète des choix de style relâchés ou particuliers et n'est pas destiné à montrer les meilleures pratiques Python.

def accept(*args):
    # wrapper for input, to satisfy the 'preferences personnelles'
    if args:
        return input(*args)
    return input()

parse_int = lambda s: int(s)

def reverse_sort(l):
    l.sort(); l.reverse()

from functools import reduce

n_m_pair = accept().split()
number_of_obj = parse_int(n_m_pair[0])
weight_limit = parse_int(n_m_pair[1])
items = {'W':[], 'V':[]}
binz = {k: [] for k in range(1,5)}
sumbinz = {k: [] for k in range(1,5)}
current_sum = {k: 0 for k in range(1,5)}

for idx in range(number_of_obj):
    nextobj = accept().split()
    items['W'] += [parse_int(nextobj[0])]
    items['V'] += [parse_int(nextobj[1])]

special_weight = items['W'][0]

for i, (w,v) in enumerate(zip(items['W'], items['V'])):
    if w-special_weight in (0,1,2,3):
        binz[w-special_weight+1].append(v)

for k in range(1,5):
    # Un idiome inhabituel ici, qui combine plusieurs étapes
    reverse_sort(binz[k])

for k in range(1,5):
    running = 0
    for elem in binz[k]:
        running+=elem
        sumbinz[k].append(running)
    sumbinz[k]=( [0]+sumbinz[k] )

from itertools import product

peak = [0]
sz = [len(sumbinz[k]) for k in range(1,5)]
# Désordre du nommage et combinatoire 4D avec un style peu orthodoxe:
for foo,bar,baz,qix in product(range(sz[3]),range(sz[2]),range(sz[1]),range(sz[0])):
    total_cnt = foo+bar+baz+qix
    wt = (special_weight)*qix + (special_weight+1)*baz + (special_weight+2)*bar + (special_weight+3)*foo
    val = sumbinz[1][qix] + sumbinz[2][baz] + sumbinz[3][bar] + sumbinz[4][foo]
    if total_cnt<=number_of_obj and wt<=weight_limit and peak[0]<val:
        # stockage valeur max dans une liste pour la mutabilité!
        peak[0]=val

print(peak[0])