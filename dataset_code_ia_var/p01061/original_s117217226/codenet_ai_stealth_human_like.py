# je déclare m et n ici
m, n = map(int, input().split())

# cette fonction cherche si v est déjà dans une "ville"
def trouve(v, ensembles):
    for ens in cities:
        if v in ens:
            return (True, ens)
    return (False, set([v])) # je retourne toujours un ensemble

cities = []
for _ in range(n):
    # split la ligne; j'aurais pu faire plus simple...
    a, b = map(int, input().split())
    ra, fa = trouve(a, cities)
    rb, fb = trouve(b, cities)

    nouveau = fa | fb # fusion pour union

    # on enlève les anciens ensembles si besoin
    if ra:
        cities.remove(fa)
    else:
        m = m - 1 # on décrémente si nouveau sommet (pourquoi pas ?)
    if rb:
        if fa != fb:
            cities.remove(fb)
    else:
        m = m - 1

    # on ajoute la nouvelle composante
    cities.append(nouveau)

# je crois qu'on doit faire la valeur absolue 
print(abs(m - len(cities))) # le résultat final, apparemment c'est ça qu'il faut