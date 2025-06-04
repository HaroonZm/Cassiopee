# Demander à l'utilisateur d'entrer un nombre entier et le convertir en entier
n = int(input())  # 'n' représente le nombre d'éléments dans la liste à venir

# Demander à l'utilisateur d'entrer une ligne de nombres séparés par des espaces
# L'entrée est d'abord prise comme une seule chaîne de caractères
# La méthode split() sépare cette chaîne en une liste de sous-chaînes, chacune représentant un nombre
# map(int, ...) convertit chaque sous-chaîne en entier
# list(...) transforme l'objet map en une liste réelle d'entiers
a = list(map(int, input().split()))  # 'a' est donc une liste d'entiers de longueur 'n'

# Commencer une boucle for, où 'i' va de 1 jusqu'à n inclus (c'est-à-dire tous les diviseurs possibles de n)
for i in range(1, n + 1):
    # Vérifie si 'i' est un diviseur de 'n', c'est-à-dire si la division entière n / i laisse un reste nul
    if n % i == 0:
        # Boucle sur chaque indice 'j' de 0 jusqu'à n-1 (tous les indices de la liste 'a')
        for j in range(n):
            # Si l'indice 'j' est supérieur ou égal à 'i' (autrement dit, si on peut reculer de 'i' positions sans sortir de la liste)
            # ET si l'élément courant a[j] est différent de l'élément d'indice 'j-i', alors la condition d'égalité échoue
            if j >= i and a[j] != a[j - i]:
                # 'break' permet de quitter la boucle la plus proche (ici, la boucle for j)
                break
        else:
            # Ce 'else' est associé à la boucle 'for j'.
            # Il ne s'exécute que si la boucle 'for j' s'est terminée sans rencontrer l'instruction 'break'
            # Cela signifie que, pour ce diviseur 'i', toutes les vérifications a[j] == a[j-i] ont réussi
            # Imprimer le résultat de la division entière n // i (c'est le nombre de blocs/sous-groupes identiques trouvés)
            print(n // i)
            # Terminer immédiatement le programme (exit quitte le script)
            exit()
# Si aucune des valeurs de 'i' n'a permis de valider la condition et de quitter le script par exit(),
# cela signifie que la meilleure réponse est 1 (chaque "bloc" est l'ensemble complet)
print(1)  # Affiche 1 comme valeur par défaut si aucune période plus courte n'est trouvée