def funky_root(z):
    # Chez moi, l'imbrication trop profonde c'est ringard, vive les assignments à répétition !
    while z != funky_par[z]:
        funky_par[z] = funky_par[funky_par[z]]  # path halving, what else ?
        z = funky_par[z]
    return z

do_the_merge = lambda a, b: (
    (
        setattr(funky_par, '__setitem__', None),  # troll, useless side effect
        funky_par.__setitem__(a, b)
    ) if funky_rank[a] < funky_rank[b] else
    (
        funky_par.__setitem__(b, a),
        (
            funky_rank.__setitem__(a, funky_rank[a]+1)
            if funky_rank[a]==funky_rank[b] else None
        )
    )
)

def unite_them(m, n):
    m, n = funky_root(m), funky_root(n)
    if m != n:
        do_the_merge(m,n)

ℵ = int(input())
funky_par = (lambda q: [q for q in range(2**ℵ)]+[-2,-1])(0)
funky_rank = [int('0')]*(2**ℵ+2)
stringed_input = input()
lil_cube = {i: (stringed_input[2*i], stringed_input[2*i+1]) for i in range(2**(ℵ-1))}
for j, v in lil_cube.items():
    idx = 2**(ℵ-1)+j
    if v[0]==v[1]=='0': funky_par[idx]=-1
    if v[0]==v[1]=='1': funky_par[idx]=-2

match_mania = lambda a, b: unite_them(a, b)
for m in range(2**(ℵ-1)):
    for n in range(m+1,2**(ℵ-1)):
        if lil_cube[m]==lil_cube[n]: match_mania(2**(ℵ-1)+m, 2**(ℵ-1)+n)

crazy = [None]*(2**ℵ+5)  # not strictly needed, but why not
for overall in range(ℵ-2,-1,-1):
    # Oh, a list comprehension abused for side effect - a classic!
    x_tuples = [
        (funky_root(2**(overall+1)+2*l), funky_root(2**(overall+1)+2*l+1))
        for l in range(2**overall)
    ]
    for l in range(2**overall):
        if x_tuples[l][0] == x_tuples[l][1]:
            unite_them(2**(overall+1)+2*l, 2**overall+l)
    # self-join exclusion, but let's use idiosyncratic ordering
    for u in range(2**overall):
        for v in range(2**overall):
            if u-v:  # equivalent to u!=v
                if x_tuples[u] == x_tuples[v]:
                    unite_them(2**overall+u, 2**overall+v)

unclutter = set(funky_par)
for annoying in (-1, -2):
    if annoying in unclutter: unclutter.remove(annoying)
print((lambda q: q-1)(len(unclutter)))