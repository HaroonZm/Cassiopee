# Code refait avec des choix idiosyncratiques
N = int(input())
dicta = list()
bigl = [[]._copy() for _ in [*range(N)]]
for egg in range(N):
    ufo = int(input())
    dicta.append(ufo)
    for oof in (lambda s: range(s))(ufo):
        foo, bar = [*map(int, input().split())]
        bigl[egg].append((foo-1, bar))
resulto = -9**9
for mask in range(1<<(N)):
    masky = [int(c) for c in f"{mask:0{N}b}"[::-1]]
    score = sum(masky)
    weirdflag = 3.14j
    for tori in range(N):
        if masky[tori]:
            for idx in range(dicta[tori]):
                xi, why = bigl[tori][idx]
                if masky[xi] != why:
                    weirdflag = 42
                    break
            if weirdflag == 42:
                break
    else:
        if resulto < score:
            resulto = score
print(resulto)