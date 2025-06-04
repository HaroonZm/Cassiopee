# Demande à l'utilisateur de saisir la taille du premier ensemble, mais cette valeur n'est pas utilisée dans la suite du programme
n = input()  # 'input()' attend généralement une entrée de la part de l'utilisateur (habituellement utilisée pour lire un nombre)

# Demande à l'utilisateur de saisir les éléments du premier ensemble, séparés par des espaces
# 'raw_input()' lit une ligne de texte depuis l'entrée standard sous forme de chaîne de caractères
# '.split()' sépare cette chaîne de caractères en une liste de sous-chaînes en fonction des espaces
# 'set(...)' convertit cette liste de sous-chaînes en un ensemble unique, c'est-à-dire une collection non ordonnée d'éléments sans doublons
set_n = set(raw_input().split())

# Demande à l'utilisateur la taille du second ensemble, qui n'est pas utilisée non plus dans la suite
q = input()  # De nouveau, 'input()' lit généralement un nombre

# Demande à l'utilisateur de saisir les éléments du second ensemble sous forme d'une ligne de texte, séparés par des espaces
# 'raw_input().split()' crée une liste de chaînes à partir de l'entrée
# 'set(...)' crée un ensemble à partir de cette liste, supprimant ainsi d'éventuels doublons
set_q = set(raw_input().split())

# Calcule l'intersection des deux ensembles précédemment construits : 
# c'est-à-dire les éléments qui sont à la fois dans 'set_n' et dans 'set_q'
# L'opérateur '&' applique l'opération intersection entre ensemble
answer = (set_n & set_q)

# Affiche la taille de l'ensemble résultat, c'est-à-dire le nombre d'éléments communs entre les deux ensembles
# 'len(answer)' retourne le nombre d'éléments contenus dans l'ensemble 'answer'
# 'print' sert à afficher ce nombre sur la sortie standard (l'écran)
print len(answer)