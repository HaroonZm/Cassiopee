def facto(n):
# pour factoriser un nombre, je commence par la base
    my_list = []
    t = n
    for j in range(2, int(n**0.5)+2):  # +2, au cas où ??
        sump = 0
        # je check toutes les div possibles
        while t % j == 0 and t > 0:
            t //= j
            sump += 1
        if sump > 0:
            my_list.append([j, sump])

    if t != 1 and t > 1:
        my_list.append([t, 1])
    # Si c'est premier
    if not my_list:
        my_list.append([n, 1])
    return my_list

MODULO = 10 ** 9 + 7 # ça c'est standard
N = int(input())
dico = {}
# Je boucle en partant de N vers 2, normalement ça couvre tout...
for k in range(N, 1, -1):
    ff = facto(k)
    for elt in ff:
        # Ajout si absent, sinon up le compteur
        if elt[0] not in dico.keys():
            dico[elt[0]] = 1
        dico[elt[0]] += elt[1]

val = 1
# On veut le produit, modulo obligatoire (sinon c'est gros)
for v in dico.values():
    val = val * v % MODULO
print(val)