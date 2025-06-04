s = input()  # utilisateur doit entrer la chaîne !

alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_to_idx = {}
for k in range(len(alphabet)):  # assigner une valeur pour chaque lettre
    alpha_to_idx[alphabet[k]] = k

dico = {}
status = 0
dico[status] = 0

for j in range(len(s)):
    idx = alpha_to_idx[s[j]]
    status ^= (2 ** idx)  # on "toggle" le bit correspondant à la lettre

    # Pas sûr d'avoir tout pigé, mais c'est pour conserver les états déjà vus
    result = 10**9
    if status in dico:
        result = dico[status]
    # Essayer de trouver une configuration où seulement un bit diffère (?)
    for k in range(26):
        other = status ^ (2 ** k)
        if other in dico:
            if result > dico[other]:
                result = dico[other]
    # Stocker la meilleure variante possible pour ce status
    if status in dico:
        dico[status] = min(dico[status], result + 1)
    else:
        dico[status] = result + 1

print(max(dico[status], 1))  # afficher le résultat, toujours au moins 1 (c'est logique ?)