# Demande à l'utilisateur de saisir une valeur, qui doit représenter un entier.
# La fonction `input()` affiche un invite (vide ici) à l'écran.
# Elle récupère la saisie utilisateur sous forme de chaîne de caractères (str).
# La fonction `int()` convertit ensuite cette chaîne de caractères en entier (int).
n = int(input())

# Initialise une variable nommée 'ans' de type chaîne de caractères (str).
# Elle contient initialement le mot "Christmas".
ans = "Christmas"

# Calcule le nombre de fois que la boucle doit s'exécuter.
# On fait '25 - n' pour déterminer combien de " Eve" il faut ajouter.
# Par exemple, si n = 24, il y aura 1 itération, si n = 23, 2 itérations, etc.
# La fonction 'range()' génère une séquence d'entiers de 0 (inclus) à 25-n (exclus).
for i in range(25 - n):
    # A chaque itération, concatène la chaîne " Eve" à la fin de la variable 'ans'.
    # L'opérateur '+=' ajoute la nouvelle chaîne à la fin de l'ancienne.
    ans += " Eve"

# Affiche la valeur finale de 'ans' à l'écran.
# Cela imprime le résultat construit de type str, composé de "Christmas" suivi du nombre approprié de " Eve".
print(ans)