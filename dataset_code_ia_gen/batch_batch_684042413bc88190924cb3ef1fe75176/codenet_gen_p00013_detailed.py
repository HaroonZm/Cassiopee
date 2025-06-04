# Solution pour le problème "Switching Railroad Cars"
# 
# Le problème consiste à simuler l'entrée et la sortie des wagons sur une voie ferroviaire.
# Chaque nombre entier représente l'entrée d'un wagon (son numéro) ou la sortie d'un wagon (0).
# 
# On modélise les wagons sur la voie comme une pile (stack) car l'ordre de sortie suit le principe LIFO :
# le dernier wagon entré est le premier à sortir.
# 
# Approche :
# - On initialise une pile vide.
# - Pour chaque entrée :
#   - Si le nombre est différent de 0, on empile (on ajoute) ce wagon.
#   - Si le nombre est 0, on dépile (on enlève et récupère) un wagon et on l'affiche.
# 
# Cette approche respecte la contrainte donnée : un 0 n'est jamais donné si la voie est vide.
# 
# Le programme s'arrête naturellement à la fin des entrées (moins de 100 lignes).

def main():
    import sys

    stack = []
    # Lire les lignes une par une
    for line in sys.stdin:
        line = line.strip()
        if not line:
            # Ligne vide possible, on ignore
            continue
        num = int(line)
        if num == 0:
            # Sortie : dépile et imprime le wagon sorti
            car = stack.pop()
            print(car)
        else:
            # Entrée : empile le wagon
            stack.append(num)

if __name__ == "__main__":
    main()