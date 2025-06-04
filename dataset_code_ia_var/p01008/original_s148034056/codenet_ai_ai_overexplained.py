# Initialisation de la variable `ans` à zéro. 
# Cette variable sera utilisée pour calculer le résultat final à l'aide de l'opération XOR (^) sur chaque valeur traitée.
ans = 0

# On va demander à l'utilisateur combien de lignes de jeu il souhaite traiter.
# La fonction `input()` affiche un prompt (ici vide), puis récupère la saisie de l'utilisateur sous forme de chaîne de caractères.
# `int()` convertit cette chaîne en un nombre entier.
# Le mot-clé `range(N)` génère une séquence de N entiers consécutifs, de 0 à N-1.
# La boucle `for` itère sur chaque valeur générée pour répéter les opérations suivantes.
for i in range(int(input())):
    # Lire une ligne entière de l'entrée standard (typiquement, le clavier).
    # `input()` lit la saisie utilisateur sous forme de chaîne de caractères unique.
    # La fonction `split()` décompose cette chaîne en une liste de mots, utilisant par défaut les espaces comme séparateurs.
    # Exemple : 'A ABC' devient ['A', 'ABC']
    p = input().split()

    # On va vérifier la longueur de la liste obtenue précédemment.
    # Si la taille de la liste est de 1, cela signifie qu'il n'y a qu'un seul élément dans la ligne saisie.
    if len(p) == 1:
        # Si c'est le cas, on crée une liste vide appelée `ms`.
        ms = []
    else:
        # Sinon, on prend le deuxième élément (indice 1) de la liste `p`, 
        # qui est supposé être une chaîne,
        # et on construit une liste `ms` contenant chacun de ses caractères individuallement.
        ms = list(p[1])
    
    # Initialisation d'une variable entière `s` qui va contenir la somme calculée dans la suite pour la ligne courante.
    s = 0
    
    # On parcourt chaque élément `m` dans la liste des caractères `ms`.
    for m in ms:
        # Si le caractère `m` représente un chiffre (0-9),
        # la méthode isdigit() retourne True.
        if m.isdigit():
            # On convertit ce caractère-chiffre en un entier avec int(m) et on l'ajoute à la somme `s`.
            s += int(m)
        # Si le caractère `m` est une lettre majuscule (A-Z), la méthode isupper() retourne True.
        elif m.isupper():
            # On convertit la lettre majuscule en une valeur entière comprise entre 10 et 35.
            # ord(m) retourne le code unicode du caractère `m`.
            # ord('A') donne le code unicode de la lettre 'A'.
            # En soustrayant ord('A') à ord(m), on obtient la position de la lettre dans l'alphabet (A=0...Z=25).
            # Comme on souhaite commencer à 10, on ajoute 10 au résultat obtenu.
            s += ord(m) - ord('A') + 10
        # Sinon, on suppose que le caractère est une lettre minuscule (a-z).
        else:
            # On convertit la lettre minuscule en une valeur entière entre 36 et 61.
            # ord(m) - ord('a') donne un indice de 0 à 25 (pour 'a' jusqu'à 'z').
            # On ajoute 36 pour obtenir la conversion souhaitée.
            s += ord(m) - ord('a') + 36
    
    # Ici, nous appliquons l'opérateur XOR (^) entre la variable globale ans et la valeur `s` calculée pour la ligne courante.
    # Cela permet d'accumuler le résultat de chaque ligne pour déterminer le vainqueur à la fin.
    ans ^= s

# À la sortie de la boucle, tous les inputs ont été traités.
# Si la variable `ans` est différente de zéro (ce qui signifie une victoire selon la règle imposée),
# on affiche le texte "win".
# Sinon, si `ans` est égal à zéro (c'est-à-dire une perte), on affiche "lose".
print("win" if ans else "lose")