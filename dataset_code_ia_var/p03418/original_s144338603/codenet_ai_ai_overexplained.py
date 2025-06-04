# Lecture de deux entiers à partir de l'entrée standard.
# La fonction input() reçoit une ligne de texte saisie par l'utilisateur.
# La méthode split() sépare cette ligne en une liste de chaînes selon les espaces.
# La fonction map(int, ...) convertit chaque élément de la liste en un entier.
# Enfin, n et k reçoivent respectivement la première et la deuxième valeur saisies.
n, k = map(int, input().split())

# Initialisation d'une variable entière appelée 'ans' pour stocker la réponse finale.
# Elle commence à 0 car on va ajouter des valeurs dessus dans la boucle.
ans = 0

# Début d'une boucle for.
# La fonction range(1, n+1) génère une séquence d'entiers commençant à 1 et allant jusqu'à n inclusivement.
# On utilise 1 comme premier argument car on veut que i commence à 1 (et non 0).
# n+1 est utilisé parce que la borne supérieure de range n'est pas incluse, alors on ajoute 1 pour inclure n.
for i in range(1, n + 1):
    # Pour chaque valeur de i entre 1 et n, on effectue les opérations suivantes :
    
    # max(i-k, 0) calcule la valeur de (i - k) mais si ce résultat est négatif, on prend 0 à la place.
    # Ceci garantit qu'on n'aura jamais de valeurs négatives ici.
    valeur_1 = max(i - k, 0)
    
    # n // i représente la division entière de n par i.
    # Cela donne combien de fois i tient "pleinement" dans n (partie entière).
    quotient = n // i
    
    # On multiplie valeur_1 (c'est-à-dire max(i-k, 0)) par le nombre de groupes entiers i dans n.
    terme_1 = valeur_1 * quotient
    
    # n % i calcule le reste de la division entière de n par i.
    # Cela donne combien il reste après avoir rempli tout ce qui tient dans des groupes de taille i.
    reste = n % i
    
    # max(n % i - k + 1, 0) prend la valeur du reste moins k puis ajoute 1,
    # Mais si ce résultat est négatif, on prend 0 à la place.
    valeur_2 = max(reste - k + 1, 0)
    
    # On additionne terme_1 et valeur_2 puis on ajoute le résultat à 'ans'.
    # C'est l'équivalent de ans = ans + (terme_1 + valeur_2).
    ans += terme_1 + valeur_2

# Après avoir terminé la boucle, on regarde la valeur de k.
# L'expression (ans if k != 0 else ans - n) signifie :
# Si k n'est PAS égal à zéro, alors on affiche ans tel quel.
# Si k EST égal à zéro, alors on affiche ans moins n.
# Ceci à cause d'une condition propre au problème qui change le résultat pour le cas k == 0.
print(ans if k != 0 else ans - n)