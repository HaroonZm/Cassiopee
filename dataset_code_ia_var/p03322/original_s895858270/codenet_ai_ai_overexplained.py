import random  # Importation du module random pour générer des nombres aléatoires, utile pour sélectionner aléatoirement des éléments dans une plage.
from collections import defaultdict  # Importation de defaultdict, qui est une classe du module collections. Elle permet de créer un dictionnaire avec une valeur par défaut retournée lorsque l’on demande une clé absente.

def solve(n, s, xs, m):
    # Initialisation d’une liste nommée 'ans' de taille n+1 où chaque élément a une valeur initiale très grande (10^9).
    # Ceci permet de garder en mémoire la plus petite valeur rencontrée à chaque position (i) lors des calculs.
    ans = [10 ** 9] * (n + 1)
    # Pour chaque valeur x dans la liste xs (on suppose que ce sont des bases indépendantes sélectionnées au hasard) :
    for x in xs:
        p = 0  # Initialisation de la position courante à zéro. Ceci servira à suivre le "curseur" logique sur une bande ou dans une séquence.
        h = 0  # Initialisation du hash courant à zéro. Le hash permet de conserver une valeur unique à chaque étape selon les opérations effectuées.
        y = 1  # Ceci représente la puissance courante de x modulo m, pour calculer rapidement les changements de hash selon la position.
        r = pow(x, m - 2, m)  # 'r' est l’inverse multiplicatif de x modulo m, utilisé pour "annuler" une multiplication par x lors du déplacement.
                              # pow(x, m-2, m) utilise le petit théorème de Fermat, car m est supposé premier : l’inverse de x modulo m est x^(m-2) mod m.
        pos = [0] * (n + 1)  # Liste pour mémoriser les positions du "curseur" après chaque instruction, initialisée à zéro.
        hashes = [0] * (n + 1)  # Liste pour mémoriser le hash calculé après chaque instruction, initialisée à zéro.
        # On parcourt la chaîne de caractères s caractère par caractère, avec un indice i partant de 1 (car enumerate(..., start=1))
        for i, c in enumerate(s, start=1):
            if c == '>':
                # Si le caractère est un '>', le curseur avance d’une position.
                p += 1
                # On multiplie y par x modulo m pour rester cohérent avec la nouvelle position.
                y = y * x % m
            elif c == '<':
                # Si le caractère est un '<', le curseur recule d’une position.
                p -= 1
                # On multiplie y par l’inverse de x (r) modulo m pour "annuler" un déplacement à droite précédent.
                y = y * r % m
            elif c == '+':
                # Si le caractère est un '+', on ajoute la valeur courante de y au hash h.
                h = (h + y) % m
            else:
                # Sinon (on suppose que le seul autre caractère possible ici est '-'), 
                # on enlève la valeur courante de y au hash h.
                h = (h - y) % m
            # On mémorise la position du curseur après cette opération.
            pos[i] = p
            # On mémorise la valeur du hash après cette opération.
            hashes[i] = h

        # On construit une liste des puissances de x modulo m, en partant de 1 jusqu’au maximum trouvé dans pos. 
        # Ceci permet d’accéder rapidement à x**k % m pour divers k.
        pow_x = [1]  # La première puissance, x^0, vaut 1.
        for _ in range(max(pos)):
            pow_x.append(pow_x[-1] * x % m)  # Chaque terme est le précédent multiplié par x modulo m.
        mp = min(pos)  # On récupère la position minimale atteinte par le curseur ; si négative, cela signifie qu’il faut aussi des puissances négatives.
        if mp < 0:
            # Si la position minimale est négative,
            # on stocke la puissance correspondante de r (= x^-1) pour x^-mp (puissance négative), en la calculant une fois.
            pow_x.append(pow(r, -mp, m))
            # Puis on continue la multiplication pour constituer la table complète des puissances nécessaires, si besoin.
            for _ in range(-mp - 1):
                pow_x.append(pow_x[-1] * x % m)

        # On récupère la valeur du hash idéal (après toutes les opérations) à la fin du parcours de s.
        ideal = hashes[-1]
        # On crée un dictionnaire avec valeur par défaut 0 pour compter l’occurrence des conditions requises.
        required = defaultdict(lambda: 0)
        # On parcourt les paires des positions et des hashs calculés (après chaque opération), avec l’indice i correspondant.
        for i, (p, h) in enumerate(zip(pos, hashes)):
            # On met à jour pour chaque position la plus petite valeur déjà rencontrée à cette position de hash : ans[i].
            ans[i] = min(ans[i], required[h])
            # On calcule la condition à remplir (appelée req), basée sur le hash idéal, la position courante et le hash à cet instant.
            req = (ideal * pow_x[p] + h) % m
            # On incrémente le compteur pour cette condition (req) dans le dictionnaire required.
            required[req] += 1

    # La fonction renvoie la somme de la liste ans. Cela réalise une agrégation finale des "meilleures" réponses pour chaque position.
    return sum(ans)

# Lecture d’un entier depuis l’entrée standard, ceci donne la longueur n de la séquence à traiter.
n = int(input())
# Lecture depuis l’entrée standard de la chaîne de caractères 's', cette chaîne sera traitée caractère par caractère.
s = input()

# On génère 3 grands entiers distincts, chacun dans l’intervalle [10^9, 10^10) pris au hasard et utilisés comme bases dans le hashing.
xs = random.sample(range(10 ** 9, 10 ** 10), 3)
# m est un très grand nombre premier (2^61 - 1 = 2305843009213693951). On l’utilise comme modulo pour minimiser le risque de collision des hashs.
m = 2305843009213693951
# On appelle la fonction solve avec tous les paramètres, puis on affiche le résultat retourné par solve.
print(solve(n, s, xs, m))