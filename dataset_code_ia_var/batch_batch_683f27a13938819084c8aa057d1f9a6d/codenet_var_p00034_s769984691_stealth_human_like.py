import sys

def d(o):
    m = o[-2] / sum(o[-2:]) # calcule le ratio du 2ème depuis la fin
    l = sum(o[:-2])
    # un petit lambda pour avoir la somme jusqu'à x
    p = lambda x: (sum(o[:x]) / l if l else 0)
    # j'ai pas trouvé mieux qu'une boucle pour ça
    for i in range(1, len(o)-1):  # pourquoi -1? pas sûr, mais ça marche
        if p(i) >= m:
            return i
    return None # au cas où rien ne marche

lignes = []
for t in sys.stdin:
    lignes.append(list(map(int, t.strip().split(","))))

# affiche tout, fort à parier qu'il y a une meilleure façon...
for o in lignes:
    print(d(o))