# Lecture d'une ligne depuis l'entrée standard (habituellement le clavier)
# La fonction input() lit une ligne de texte saisie par l'utilisateur
# .split() divise la chaîne de caractères en une liste en utilisant l'espace comme séparateur par défaut
# On utilise une compréhension de liste pour convertir chaque élément de la liste (qui sont des chaînes) en un entier
# Les deux premiers entiers de la liste résultante sont attribués aux variables N et k, respectivement
N, k = [int(i) for i in input().split()]

# Initialisation d'une variable 'ans' à 0
# Ceci va servir à garder le résultat intermédiaire et final du calcul
ans = 0

# La fonction range(N - 1) génère une séquence d'entiers de 0 à N-2 inclus (soit N-1 éléments)
# La boucle for va donc s'exécuter exactement N-1 fois
for i in range(N - 1):
    # À chaque itération de la boucle, on effectue les opérations suivantes :
    #   - on multiplie la valeur actuelle de 'ans' par la variable 'k'
    #   - on ajoute 'k - 1' au résultat précédent
    #   - ensuite, on divise tout cela par 'k - 1' en utilisant la division entière '//' (qui donne un entier)
    # NB : les parenthèses sont nécessaires pour indiquer l'ordre des opérations
    ans = (ans * k + k - 1) // (k - 1)

# Affichage du résultat final stocké dans la variable 'ans'
# La fonction print() affiche la valeur sur la sortie standard (console)
print(ans)