# Lecture de quatre entiers séparés par des espaces sur une seule ligne d'entrée utilisateur.
# Ces entiers sont affectés respectivement aux variables L, A, B, M.
L, A, B, M = map(int, input().split())

# Définition d'une fonction appelée 'partsum' qui prend 4 arguments nommés a, b, l, n.
def partsum(a, b, l, n):
    # Création d'une liste 'doublingconst' de taille 60 remplie d'entiers zéro.
    # Cette liste stocke des valeurs utilisées pour une technique appelée 'doublage' inspirée de l'exponentiation rapide.
    doublingconst = [0 for i in range(0, 60)]
    # On initialise le premier élément (indice 0) de la liste à 1.
    # Cela sert de base pour la technique du doublage ci-après.
    doublingconst[0] = 1

    # Création d'une autre liste 'doublingline' de taille 60 remplie d'entiers zéro.
    # Cette liste va stocker des contributions additionnelles liées à la progression linéaire dans la construction du nombre.
    doublingline = [0 for i in range(0, 60)]
    # On initialise le premier élément à 0.
    doublingline[0] = 0

    # Boucle for allant de 1 à 59 inclus, c'est-à-dire pour chaque puissance de 2 jusqu'à 2^59, utilisée pour la technique du doublage.
    for i in range(1, 60):
        # Calcul de nouvelles valeurs dans doublingconst (contribution constante du bloc) :
        # pow(10, l*2**(i-1), M) calcule le reste (modulo M) de 10 à la puissance l fois 2^(i-1).
        # On ajoute 1 à ce résultat, puis on multiplie par la valeur précédente de doublingconst, et on prend le modulo M.
        doublingconst[i] = (
            (pow(10, l * 2 ** (i - 1), M) + 1) * doublingconst[i - 1] % M
        )

        # Calcul de nouvelles valeurs dans doublingline (contribution linéaire du bloc) :
        # pow(2, i-1, M) calcule 2^(i-1) modulo M.
        # On multiplie par pow(10, l*2**(i-1), M) (c'est-à-dire un décalage de chiffres en base 10), 
        # puis on multiplie par doublingconst[i-1]. Ce terme est ajouté à la précédente valeur de doublingline multipliée par
        # (pow(10, l*2**(i-1), M) + 1), puis modulo M.
        doublingline[i] = (
            (pow(10, l * 2 ** (i - 1), M) + 1) * doublingline[i - 1]
            + pow(2, i - 1, M) * pow(10, l * 2 ** (i - 1), M) * doublingconst[i - 1]
        ) % M

    # Initialisation de la variable qui cumulera la contribution "constante" totale.
    ansconst = 0
    # Initialisation du décalage 'chousei' (qui veut dire "ajustement" en japonais).
    chousei = 0

    # On effectue la décomposition binaire du nombre n (nombre de blocs à traiter).
    # À chaque bit 'i' à 1 dans n, on empile la contribution du 2^i-ème bloc via le doublage.
    for i in range(0, 60):
        # Test pour savoir si le i-ème bit est à 1 dans n : (n>>i &1 == 1)
        # L'opérateur '>>' réalise un décalage binaire à droite ; '& 1' isole le bit de poids faible.
        if n >> i & 1 == 1:
            # Ajout de la contribution constante de ce bloc, ajustée d'un décalage de puissance de 10 (décalage en base 10).
            ansconst += doublingconst[i] * pow(10, chousei * l, M)
            # Réduction modulo M pour maintenir la taille du nombre raisonnable.
            ansconst %= M
            # On augmente 'chousei' de 2^i, car on vient de traiter 2^i blocs de longueur l.
            chousei += 2 ** i

    # On recommence le même processus pour la contribution "linéaire".
    ansline = 0
    chousei = 0
    for i in range(0, 60):
        if n >> i & 1 == 1:
            # Ajout de la contribution issue du doublage, plus un terme de correction dépendant du décalage.
            ansline += (
                (doublingline[i] + chousei * doublingconst[i]) * pow(10, chousei * l, M)
            )
            ansline %= M
            chousei += 2 ** i

    # Renvoie la combinaison linéaire des contributions (poids a et b), comme retour de la fonction.
    return ansline * a + ansconst * b

# Détermination de la longueur (en nombre de chiffres) du nombre de départ A.
start = len(str(A))
# Détermination de la longueur (en nombre de chiffres) du dernier nombre généré (B*L + A - B).
end = len(str(B * L + A - B))

# Création d'une liste vide pour stocker les informations sur les "parties" à traiter.
# Chaque partie correspond à une plage de nombres ayant le même nombre de chiffres.
part = []

# Boucle qui va itérer du nombre de chiffres minimal de départ (start-1) à celui de fin (end - 1) inclus.
for i in range(start - 1, end):
    # Calcul de l'indice l (premier numéro de bloc atteignant le nombre de chiffres i+1), basé sur les propriétés de la suite arithmétique générée.
    l = 1 + (10 ** i - A - 1) // B
    # Calcul de l'indice r (dernier numéro de bloc pour i+1 chiffres),
    r = (10 ** (i + 1) - A - 1) // B
    # Correction pour que l ne soit pas en dessous de 0, grâce à la fonction max.
    l = max(0, l)
    # Correction pour que r ne dépasse pas L-1, grâce à la fonction min.
    r = min(L - 1, r)
    # Ajout d'une sous-liste contenant (nombre de chiffres, borne gauche l, borne droite r).
    part.append([i + 1, l, r])

# Tri de la liste part en ordre décroissant selon la longueur du nombre (part[i][0]) pour traitement ultérieur.
part.sort(reverse=True)

# Initialisation du résultat final à 0.
ans = 0
# Initialisation d'une variable 'chousei', représentant le nombre total de chiffres déjà produits,
# pour ajuster le décalage en base 10 pour la prochaine portion.
chousei = 0

# Parcours de chaque intervalle stocké dans la liste 'part' traitée.
for i in range(0, len(part)):
    # Décomposition de chaque sous-liste en variables 'length' (nombre de chiffres des nombres concernés), l, r.
    length, l, r = part[i]
    # Calcul de la valeur de départ (const) pour la séquence correspondante (dernier nombre de l'intervalle).
    const = B * r + A
    # Le pas de la suite arithmétique (line), qui est B (constance de l'écart entre les termes consécutifs).
    line = B
    # Addition au résultat final, pour cette portion :
    # - appel à partsum() qui va calculer la contribution de cette portion (nombre, positions, etc.),
    # - pow(10, chousei, M) multiplie par la bonne puissance de 10 selon tous les chiffres déjà traités,
    # - prise du modulo M après chaque addition majeure pour garder la taille du nombre sous contrôle.
    ans += (partsum(-line, const, length, r - l + 1) * pow(10, chousei, M)) % M
    ans %= M
    # Incrémentation du décalage 'chousei' par le nombre de chiffres produits dans cette portion (nombre de nombres * longueur de chaque nombre).
    chousei += length * (r - l + 1)

# Après avoir traité toutes les portions, affichage du résultat final.
print(ans)