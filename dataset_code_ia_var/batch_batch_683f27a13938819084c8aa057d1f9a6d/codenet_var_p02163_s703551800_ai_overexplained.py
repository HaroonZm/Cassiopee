# Demande à l'utilisateur d'entrer un nombre entier et convertit l'entrée en entier
N = int(input())

# Initialisation de deux variables : 'a' est défini à 1 et 'b' à 0
# 'a' et 'b' vont servir à stocker des valeurs qui seront modifiées dans la boucle
a = 1
b = 0

# Boucle for qui va s'exécuter N fois
for _ in range(N):
    # Demande à l'utilisateur d'entrer deux nombres séparés par un espace
    # Les deux nombres sont convertis en entiers et assignés respectivement à q et x
    q, x = map(int, input().split())
    
    # Vérifie si la valeur de q est égale à 1
    if q == 1:
        # Met à jour la valeur de 'a' en la multipliant par 'x'
        a = a * x
        # Met également à jour la valeur de 'b' en la multipliant par 'x'
        b = b * x
    # Si q n'est pas 1 mais 2
    elif q == 2:
        # Ajoute 'x' à la variable 'b' (incrémentation)
        b = b + x
    # Si q n'est ni 1 ni 2 (donc prend la 3ème valeur possible ici)
    else:
        # Soustrait 'x' à la variable 'b' (décrémentation)
        b = b - x

# Affiche le résultat final sous la forme de deux valeurs séparées par un espace
# La première valeur affichée est l'opposé de 'b' (on place donc un signe moins devant b)
# La seconde valeur est la valeur actuelle de 'a'
print(-b, a)