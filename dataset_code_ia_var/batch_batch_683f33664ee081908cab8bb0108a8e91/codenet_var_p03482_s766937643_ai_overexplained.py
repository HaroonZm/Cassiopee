# Demande à l'utilisateur de saisir une chaîne de caractères via l'entrée standard (clavier).
# 'input()' lit tout ce que l'utilisateur tape jusqu'à validation avec "Entrée".
# Le résultat (une chaîne de caractères) est stocké dans la variable 's'.
s = input()

# Calcule la moitié entière (division entière par 2) de la longueur de la chaîne 's'.
# 'len(s)' donne la longueur de la chaîne (nombre de caractères).
# '//' réalise une division entière (seul le quotient est conservé, la partie décimale est ignorée).
# Exemple : pour une chaîne de longueur 7, 7 // 2 == 3.
# Stocke la valeur obtenue dans la variable 'cnt'.
cnt = len(s) // 2

# Crée une variable 'i' initialisée à zéro.
# 'i' va servir à parcourir la chaîne autour de sa position centrale, de façon symétrique.
i = 0

# Vérifie si la longueur de la chaîne 's' est impaire.
# 'len(s) % 2' donne le reste de la division par 2 de la longueur de la chaîne.
# Si la longueur est impaire, le résultat sera 1 (considéré comme vrai dans une condition).
if len(s) % 2:
    # Si la longueur est impaire, entre dans cette boucle while.
    # La boucle va s'exécuter tant que deux conditions sont réunies :
    # 1. 'cnt + i < len(s)' : s'assure qu'on ne dépasse pas la fin de la chaîne à droite.
    # 2. 's[cnt - i] == s[cnt + i] == s[cnt]' :
    #    Vérifie que le caractère 's[cnt - i]' (à gauche du centre),
    #    le caractère 's[cnt + i]' (à droite du centre) et le caractère 's[cnt]'
    #    (le centre lui-même) sont tous identiques.
    while cnt + i < len(s) and s[cnt - i] == s[cnt + i] == s[cnt]:
        # Si les conditions sont remplies, incrémente 'i' pour élargir la comparaison sur la séquence centrale.
        i += 1
else:
    # Si la longueur est paire, c'est ce bloc qui est exécuté.
    # On modifie légèrement les indices pour rester symétrique autour des deux caractères du milieu.
    # 's[cnt - i - 1]' est le caractère à gauche du centre,
    # 's[cnt + i]' est le caractère à droite du centre,
    # 's[cnt]' est le caractère situé juste après le centre gauche.
    while cnt + i < len(s) and s[cnt - i - 1] == s[cnt + i] == s[cnt]:
        # Tant que les conditions ci-dessus sont vraies, on élargit les comparaisons.
        i += 1

# Après avoir terminé la boucle, 'i' contient le nombre de caractères identiques (de part et d'autre du centre, incluant le centre),
# et 'cnt' est le point de départ du motif palindromique central (pour les chaînes impaires) ou juste après le centre gauche (pour les chaînes paires).
# On affiche alors la somme 'cnt + i', qui représente la longueur maximale, à partir du début,
# pour laquelle il existe une séquence symétrique centrale constituée du même caractère.
print(cnt + i)