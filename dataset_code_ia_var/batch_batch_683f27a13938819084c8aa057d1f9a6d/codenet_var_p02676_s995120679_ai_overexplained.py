# Demande à l'utilisateur de saisir un nombre entier pour K
# input() lit une entrée depuis le clavier sous forme de chaîne de caractères
# int() convertit cette chaîne en un nombre entier
K = int(input())

# Demande à l'utilisateur de saisir une chaîne de caractères pour S
# input() lit l'entrée et la stocke telle quelle dans la variable S (aucune conversion nécessaire ici)
S = input()

# On vérifie si la longueur de la chaîne S est inférieure ou égale à K
# len(S) donne le nombre de caractères dans S
if len(S) <= K:
    # Si la longueur de S est inférieure ou égale à K, 
    # on affiche simplement S tel quel à l'aide de la fonction print()
    print(S)
else:
    # Sinon (donc si la longueur de S est strictement supérieure à K),
    # on tronque S pour ne garder que les K premiers caractères à l'aide de la notation de tranche S[:K]
    # Puis on ajoute une chaîne de trois points de suspension "..." pour indiquer que S a été coupé
    S = S[:K] + "..."
    # On affiche la nouvelle valeur de S, tronquée et suivie des points de suspension
    print(S)