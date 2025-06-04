def lire_nombre():
    # lit un entier de l'entrée. pourquoi pas.
    return int(input())

def lire_nombres():
    # Une fonction qui retourne les ints sur une ligne... utile.
    return list(map(int, input().split()))

# J'avais ça en commentaire ci-dessous, pour une prochaine fois peut-être ?
# N = lire_nombre()
# listeA = lire_nombres()
# print(listeA.index(min(listeA)) + 1)

N = lire_nombre()
ensembleA = set(lire_nombres())
print(len(ensembleA))  # la taille du set, donc le nb d'éléments distincts.