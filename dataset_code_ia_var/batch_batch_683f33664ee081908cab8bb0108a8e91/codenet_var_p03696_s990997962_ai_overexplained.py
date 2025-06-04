# Définition d'une fonction pour lire deux entiers à partir d'une ligne d'entrée standard
def two_int():
    # La fonction `input()` lit une ligne au clavier (entrée standard)
    # La méthode `split()` découpe la ligne en sous-chaînes à chaque espace
    # Ensuite, `map(int, ...)` convertit chaque sous-chaîne en entier
    N, K = map(int, input().split())
    # Cette fonction retourne un tuple contenant deux entiers : N et K
    return N, K

# Définition d'une fonction pour lire un seul entier de l'entrée
def one_int():
    # Ici, on utilise encore `input()` pour lire une ligne
    # Puis on convertit simplement cette ligne en un entier grâce à `int()`
    return int(input())

# Définition d'une fonction pour lire une seule chaîne de caractères de l'entrée
def one_str():
    # Utilise `input()` pour lire et retourner la chaîne telle quelle
    return input()

# Définition d'une fonction pour lire plusieurs entiers sur une ligne d'entrée
def many_int():
    # Ici, comme pour `two_int`, on lit la ligne et on la découpe en éléments 
    # Ensuite, chaque élément est converti en entier
    # Enfin, le résultat est transformé en liste grâce à `list()`
    return list(map(int, input().split()))

# -- Début du programme principal --

# Lecture d'un entier à partir de l'entrée
# Cela stocke la valeur entière entrée par l'utilisateur dans la variable N
N = one_int()

# Lecture d'une chaîne de caractères à partir de l'entrée
# Cela stocke la chaîne entrée par l'utilisateur dans la variable S
S = one_str()

# Initialisation d'une variable 'head' qui comptera combien de parenthèses ouvrantes supplémentaires
# il faut éventuellement ajouter au début de la chaîne pour équilibrer
head = 0

# Initialisation d'une variable 'tail' qui n'est pas utilisée dans ce code (reste à zéro)
# Cette variable pourrait servir à compter les parenthèses fermantes à rajouter à la fin,
# mais dans ce programme on utilise directement une autre méthode.
tail = 0

# Définition d'une variable 'point' qui suivra en temps réel le nombre de parenthèses ouvertes sans fermeture
# Cette variable sera incrémentée chaque fois qu'on rencontre une parenthèse ouvrante "("
# et décrémentée en rencontrant une parenthèse fermante ")"
point = 0

# Boucle for pour parcourir chaque caractère 'a' de la chaîne S
for a in S:
    # Si le caractère courant est une parenthèse ouvrante
    if a == "(":
        # Incrémente 'point' de 1, indiquant une parenthèse ouverte supplémentaire non fermée
        point += 1
    else:
        # Ici, on suppose qu'il s'agit d'une parenthèse fermante ")"
        # On décrémente 'point' de 1, car une parenthèse ouverte est maintenant fermée
        point -= 1
    # Vérification si le nombre de parenthèses fermantes dépasse le nombre d'ouvrantes à ce stade
    if point < 0:
        # Si oui, cela signifie qu'une parenthèse fermante ne correspond à aucune ouvrante
        # On compte le nombre de parenthèses ouvrantes à rajouter au début de la chaîne pour compenser
        head += 1
        # On corrige 'point' en l'incrémentant de 1 pour simuler l'ajout d'une parenthèse ouvrante avant
        # Cela revient à annuler la situation négative et repartir à zéro
        point += 1

# Après la boucle, 'head' contient le nombre de parenthèses ouvrantes à ajouter au DEBUT
# 'point' contient la différence (positive) entre le nombre d'ouvrantes et de fermantes,
# donc on doit ajouter ce nombre de parenthèses fermantes à la FIN pour équilibrer

# On utilise 'print' pour afficher le résultat final :
# - On multiplie la chaîne "(" par 'head' pour obtenir le bon nombre de parenthèses en début de chaîne
# - On concatène la chaîne d'origine S
# - On ajoute 'abs(point)' fois la chaîne ")" pour équilibrer ce qui manque à la fin
print("(" * head + S + abs(point) * ")")