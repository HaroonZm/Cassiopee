import sys

# On lit toutes les lignes depuis l'entrée standard
lines = sys.stdin.read().strip().split('\n')

# Chaque dataset est constitué de deux lignes : 
# première ligne les 4 nombres imaginés par A
# deuxième ligne les 4 nombres choisis par B
# On traite les lignes deux par deux
for i in range(0, len(lines), 2):
    # Récupérer les nombres imaginés par A et par B sous forme de listes d'entiers
    a = list(map(int, lines[i].split()))
    b = list(map(int, lines[i+1].split()))
    
    # Calcul du nombre de Hit:
    # Un "Hit" est lorsque le chiffre à la même position est identique
    hit = sum(1 for x, y in zip(a, b) if x == y)
    
    # Calcul du nombre de Blow:
    # Un "Blow" est un chiffre présent dans a ET b mais pas à la même position
    # On compte tous les chiffres communs, puis on soustrait le nombre de Hit pour garder les Blow
    # Comme les chiffres sont distincts dans chaque liste, on peut utiliser l'ensemble d'intersection
    common = set(a) & set(b)
    blow = len(common) - hit
    
    # Affichage du résultat
    print(hit, blow)