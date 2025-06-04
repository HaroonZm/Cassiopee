# Cette fonction 'plus' met à jour le vecteur de compte global 'c' en fonction du caractère 's' passé en paramètre
def plus(s):
    # On indique que la variable 'c' qu'on va modifier dans cette fonction est la même que celle définie en dehors de la fonction (au niveau global)
    global c
    # On crée une nouvelle liste 'd' de longueur 7, initialisée avec des zéros.
    # Cette liste 'd' va servir à stocker les nouveaux comptes calculés avant de remplacer l'ancienne 'c'
    d = [0] * 7  # [0, 0, 0, 0, 0, 0, 0]
    # On parcourt toutes les valeurs possibles d'indices 'i' de 0 à 6 (inclus), c'est-à-dire pour chaque élément de 'g'.
    for i in range(7):
        # On vérifie si le caractère 's' est dans le set 'g[i]'.
        # Par exemple, 'g[i]' peut être {"J"} ou {"J", "O"}, etc.
        if s in g[i]:
            # Si c'est le cas, on veut mettre à jour le compteur correspondant à la position 'i'
            # On parcourt tous les indices possibles 'j' de 0 à 6 pour prendre en compte toutes les transitions possibles entre les états représentés par les ensembles 'g'
            for j in range(7):
                # On vérifie si l'intersection entre 'g[i]' et 'g[j]' n'est pas vide (set vide = set()).
                # Cela signifie qu'on veut seulement considérer les états 'j' qui partagent au moins une lettre avec le nouvel état 'i'
                if g[i] & g[j] != set():
                    # Si la condition est respectée, on ajoute le nombre de façons d'atteindre l'état 'j' à celui de l'état 'i'
                    # c[j] contient le nombre de manières d'arriver à l'état 'j' avant ce caractère
                    d[i] += c[j]
    # Après avoir calculé tous les nouveaux comptages, on affecte la liste 'd' à la variable globale 'c'
    # 'c' reflète désormais le nouvel état après avoir pris en compte la lettre courante 's'
    c = d

# Lecture du nombre d'étapes ou du nombre de caractères à traiter ('n') à partir de l'entrée standard (clavier).
# La fonction input() lit une ligne de texte et int() convertit ce texte en un entier
n = int(input())
# Lecture de la chaîne de texte d'entrée. On suppose ici que la chaîne a une longueur d'au moins 'n' caractères.
s = input()
# On définit la liste 'g', contenant sept ensembles différents. Chaque ensemble contient les lettres liées à un certain état ou combinaison de lettres.
# Ces ensembles servent à représenter les groupes de lettres qui peuvent se chevaucher ou être combinés.
g = [
    set(["J"]),             # premier état: ensemble contenant seulement 'J'
    set(["O"]),             # deuxième état: ensemble contenant seulement 'O'
    set(["I"]),             # troisième état: ensemble contenant seulement 'I'
    set(["J", "O"]),        # quatrième état: ensemble contenant 'J' et 'O'
    set(["J", "I"]),        # cinquième état: ensemble contenant 'J' et 'I'
    set(["O", "I"]),        # sixième état: ensemble contenant 'O' et 'I'
    set(["J", "O", "I"])    # septième état: ensemble contenant 'J', 'O', et 'I'
]
# On définit la liste des comptes 'c', qui va représenter le nombre de manières différentes d'enchaîner les lettres jusqu'à chaque état.
# Initialement, on démarre avec une façon ('1') d'être dans le premier état (par convention ou pour respecter la contrainte initiale du problème)
# Les autres états sont mis à zéro puisque, au début, on ne peut pas être dans d'autres états.
c = [1, 0, 0, 0, 0, 0, 0, 0]  # liste de longueur 8, le dernier élément est inutile pour ce problème car on n'utilise que les indices 0 à 6
# On itère sur chaque caractère de la chaîne 's', exactement 'n' fois.
for i in range(n):
    # On passe le i-ème caractère de la chaîne 's' à la fonction plus.
    # La fonction mettra à jour 'c' suivant la logique décrite plus haut.
    plus(s[i])

# Finalement, on calcule la somme des comptes dans la liste 'c'.
# La fonction sum(c) additionne tous les éléments de la liste 'c'.
# On effectue un modulo 10007 sur ce résultat pour éviter de dépasser certaines limites (typiquement imposées dans les problèmes de programmation compétitive)
# On affiche ce résultat à l'écran à l'aide de la fonction print()
print(sum(c) % 10007)