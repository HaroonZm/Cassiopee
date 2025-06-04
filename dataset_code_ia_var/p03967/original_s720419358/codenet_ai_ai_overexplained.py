# Demande à l'utilisateur d'entrer une chaîne de caractères et stocke la valeur saisie dans la variable S.
S = input()

# Initialise la variable 'ans' à 0. Cette variable va servir à garder un compte, ou score,
# qui sera ajusté en fonction de chaque caractère de la chaîne S analysé selon des règles précises.
ans = 0

# On utilise une boucle for pour itérer sur chaque index 'i' de la chaîne S.
# 'range(len(S))' génère une séquence d'entiers de 0 jusqu'à la longueur de S non incluse,
# ce qui permet d'accéder à chaque caractère de S individuellement via son positionnement dans la chaîne.
for i in range(len(S)):
    # PremiÈre condition : 
    # On vérifie si 'i' est pair en utilisant l'opérateur modulo : 'i % 2 == 0'.
    # Cela signifie qu'on veut cibler les positions 0, 2, 4, ... de la chaîne.
    # De plus, on vérifie simultanément si le caractère à cette position dans S, c'est-à-dire S[i], est la lettre 'p'.
    if i % 2 == 0 and S[i] == "p":
        # Si les deux conditions sont vraies (i pair ET caractère 'p'), 
        # alors on décrémente la variable 'ans' de 1. 
        # Cela signifie que l'on retire 1 du score actuel.
        ans -= 1
    # Dans le cas où la première condition n'est pas satisfaite, on vérifie l'alternative suivante :
    # On regarde si 'i' est impair ('i % 2 == 1'), c'est-à-dire pour les positions 1, 3, 5, ...
    # en même temps que le caractère correspondant dans S, c'est-à-dire S[i], est la lettre 'g'.
    elif i % 2 == 1 and S[i] == "g":
        # Si les deux conditions sont vraies (i impair ET caractère 'g'), 
        # alors on incrémente la variable 'ans' de 1.
        # Cela signifie que l'on ajoute 1 au score actuel.
        ans += 1

# Après avoir traité tous les caractères de la chaîne S (la boucle est terminée), 
# on affiche la valeur finale de la variable 'ans' à l'écran en utilisant la fonction print.
print(ans)