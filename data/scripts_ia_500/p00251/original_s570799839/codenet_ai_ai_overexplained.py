# Initialisation de la variable 'sum' à 0.
# Cette variable servira à stocker la somme cumulée des nombres que l'utilisateur va saisir.
sum = 0

# Boucle 'for' qui s'exécute 10 fois.
# 'range(10)' génère une séquence de nombres allant de 0 à 9 (total 10 valeurs).
# La variable 'i' prend successivement chacune de ces valeurs, mais ici elle n'est pas utilisée directement.
for i in range(10):
    # Demande à l'utilisateur d'entrer une valeur via la fonction 'input()'.
    # 'input()' capture la saisie de l'utilisateur sous forme de chaîne de caractères (string).
    # La fonction 'int()' convertit cette chaîne en un entier.
    s = int(input())
    
    # Ajoute la valeur entière saisie (s) à la variable 'sum'.
    # L'opérateur '+=' est un opérateur d'affectation combiné qui équivaut à : sum = sum + s
    sum += s

# Affiche la valeur finale de 'sum' après les 10 itérations.
# La fonction 'print()' convertit automatiquement la valeur en chaîne de caractères pour l'affichage.
print(sum)