# Demander à l'utilisateur de saisir un nombre entier et stocker la valeur dans la variable N.
# La fonction int() convertit la chaîne saisie par input() en un entier.
N = int(input())

# Créer un dictionnaire D qui sert à associer les valeurs booléennes True et False
# à des caractères correspondants. Ici, True est associé à la lettre 'S' et 
# False à la lettre 'W'. Cette association sera utilisée plus tard pour convertir
# les valeurs booléennes dans une représentation sous forme de caractères.
D = {True: 'S', False: 'W'}

# Créer un dictionnaire E qui convertit les caractères 'o' et 'x' en des valeurs booléennes.
# 'o' représente True, 'x' représente False.
# Ceci sert à transformer une chaîne du type 'oxxo' en une liste de booléens.
E = {'o': True, 'x': False}

# Lire une chaîne de caractères via input() et la transformer en une liste de caractères individuels,
# ainsi S contiendra chaque lettre de la saisie séparément.
S = list(input())

# Boucler sur chaque indice de la liste S (de 0 à N-1)
for i in range(N):
    # Remplacer à chaque position le caractère par sa valeur booléenne correspondante
    # selon le dictionnaire de conversion E. Par exemple, 'o' devient True, 'x' devient False.
    S[i] = E[S[i]]

# Définir un ensemble L contenant toutes les combinaisons possibles de deux valeurs booléennes.
# Chaque élément du set L est un tuple (a, b). Il y a 4 possibilités : 
# (True, True), (True, False), (False, True), et (False, False).
L = {
    (True, True),
    (True, False),
    (False, True),
    (False, False)
}

# Pour chaque combinaison possible de (a, b) dans l'ensemble L :
for a, b in L:
    # Créer une liste ans de taille N initialisée avec la valeur None à chaque position.
    # Cette liste sera utilisée pour stocker la solution candidate construite à partir de (a, b).
    ans = [None] * N
    
    # Initialiser les deux premiers éléments de la liste ans avec les valeurs de a et b
    # Cela fixe les deux premiers animaux sous les états (True/False) choisis par la boucle.
    ans[0], ans[1] = a, b
    
    # Boucler sur chaque indice i allant de 1 jusqu'à N-2 inclus (c'est-à-dire, de 1 à N-2).
    # On démarre à i = 1 car les deux premiers éléments ans[0] et ans[1] sont déjà fixés.
    for i in range(1, N - 1):
        # Vérifier le résultat du XOR (^) entre ans[i] et S[i].
        # L'opérateur XOR en Python renvoie True si les deux opérandes sont différents, False sinon.
        # L'expression "not ans[i] ^ S[i]" est donc True s'ils sont identiques.
        if not ans[i] ^ S[i]:
            # Si ans[i] et S[i] sont identiques, alors le prochain état ans[i+1] prend la valeur ans[i-1].
            ans[i + 1] = ans[i - 1]
        else:
            # Sinon, ans[i+1] prend la valeur "non ans[i-1]", c'est-à-dire le contraire de ans[i-1].
            ans[i + 1] = not ans[i - 1]
    
    # Après avoir généré toute la liste ans, il faut vérifier si la configuration trouvée est cohérente.
    # Cette vérification repose sur le fait que la séquence est cyclique, donc il faut vérifier 
    # la cohérence entre les deux extrémités de la liste selon deux conditions :
    # 1. ans[-1] ^ S[-1] == ans[-2] ^ ans[0] vérifie la cohérence en tenant compte du dernier, 
    #    avant-dernier, et du premier élément.
    # 2. ans[0] ^ S[0] == ans[-1] ^ ans[1] vérifie la cohérence entre le début et la fin de la séquence.
    if ans[-1] ^ S[-1] == ans[-2] ^ ans[0] and ans[0] ^ S[0] == ans[-1] ^ ans[1]:
        # Si la configuration est cohérente, on convertit à chaque position la valeur booléenne
        # de ans en la lettre correspondante ('S' ou 'W') grâce au dictionnaire D.
        for i in range(N):
            ans[i] = D[ans[i]]
        # On affiche la séquence sous forme de chaîne de caractères, en collant tous les caractères ensemble.
        print(''.join(ans))
        # On arrête le programme immédiatement, car une solution valide a été trouvée.
        exit()
# Si la boucle for a parcouru toutes les possibilités sans trouver de solution cohérente,
# le bloc else du for s'exécute (il est lié au for, pas au if !). On affiche alors -1 pour indiquer l'échec.
else:
    print(-1)