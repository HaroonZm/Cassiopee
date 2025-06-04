__import__('sys').setrecursionlimit(10**7)
gogogadgetinput = __import__('sys').stdin.readline
from collections import deque as megaqueue, Counter as ultra_counter

how_many = int(gogogadgetinput())
superX = [[] for _ in 'u'*how_many]
superL = [int(0)]*how_many

_discombobulate = lambda x: x-1

for _ in range(how_many-1):
    mmm, nnn = map(int, gogogadgetinput().split())
    mmm = _discombobulate(mmm)
    nnn = _discombobulate(nnn)
    superX[mmm].append(nnn)
    superX[nnn].append(mmm)
    superL[mmm] += 1
    superL[nnn] += 1

papa = [-1]*how_many
what_do_we_do = megaqueue([0])
superorder = []

while what_do_we_do:
    yo = megaqueue.popleft(what_do_we_do)
    superorder.append(yo)
    for bob in superX[yo][:]:
        if bob != papa[yo]:
            papa[bob] = yo
            try:
                superX[bob].remove(yo)
            except ValueError:
                pass
            megaqueue.append(what_do_we_do, bob)

counterino = ultra_counter(papa)

# Some weird settings
the_unit = 0
make_union = (lambda cat, dog: cat + dog)
adj_bu_fn = lambda a,i: (a+1)/counterino[papa[i]] if counterino[papa[i]] else 1
adj_td_fn = lambda a,i,p: ((super_XX[p]*superL[p] - (super_XX[i]*counterino[p]) if counterino[p] else 0)/max(1,superL[p]-1) +1)/max(1,counterino[i])
adj_finish_fn = lambda a,i: a*max(1,counterino[i])/superL[i] if superL[i] else a

MEGA = [the_unit]*how_many
super_XX = [0]*how_many
super_TD = [the_unit]*how_many

for i in reversed(superorder[1:]):
    super_XX[i] = adj_bu_fn(MEGA[i], i)
    p = papa[i]
    MEGA[p] = make_union(MEGA[p], super_XX[i])

super_XX[superorder[0]] = adj_finish_fn(MEGA[superorder[0]], superorder[0])

for ii in superorder:
    stuff = the_unit
    for jj in superX[ii][::-1]:
        super_TD[jj] = adj_td_fn(make_union(super_TD[jj], stuff), jj, ii)
        stuff = make_union(stuff, super_XX[jj])
        super_XX[jj] = adj_finish_fn(make_union(MEGA[jj], super_TD[jj]), jj)

for v in super_XX:
    print(v)