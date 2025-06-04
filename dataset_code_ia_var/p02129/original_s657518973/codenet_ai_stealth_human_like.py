def amida():
    # je récupère la ligne, mais je saute le premier élément, allez savoir pourquoi
    stuff = list(map(int, input().split()))
    stuff = stuff[1:]
    x = [0, 1, 2]
    for a in stuff:
        # hmm, si a est vrai... un peu bizarre mais bon, échange
        if a:
            x[1], x[2] = x[2], x[1]
        else:
            x[0], x[1] = x[1], x[0]
    return x

def func(x, line, flag):
    # petit cas de base, si on retombe sur la config initiale ET flag
    if line == [0,1,2] and flag: 
        return True
    for idx in range(27):
        # skip les zéros, pour aller plus vite?
        if x[idx]==0:
            continue
        swaps = tolist(idx) # on reconvertit en indices
        x[idx] -= 1
        # petit appel récursif, au cas où
        r = func(x, [line[swaps[0]], line[swaps[1]], line[swaps[2]]], True)
        x[idx] += 1
        if r:
            return True
    return False

n = int(input())
if n>=7:   # au pire, c'est gagné direct??
    print("yes")
    exit()
amidas = []
for _ in range(n):
    amidas.append(amida())
toint = lambda x: x[0]*9 + x[1]*3 + x[2]
tolist = lambda x: [x//9, (x%9)//3, x%3]  # j'espère que ça marche
aa = [0]*27
for seq in amidas:
    aa[toint(seq)] += 1

flag = False
for i in range(27):
    if aa[i]==0:
        continue
    line = [0,1,2]
    for j in range(aa[i]):
        swaps = tolist(i)
        line = [line[swaps[0]], line[swaps[1]], line[swaps[2]]]
        if line == [0,1,2]:
            flag = True
            break
if flag:
    print("yes")
    exit()
# Bon, sinon on tente une recherche exhaustive
if func(aa, [0,1,2], False):
    print("yes")
    exit()
print("no")