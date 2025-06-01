# Initialisation de la variable 'S' avec la valeur 0
# Cette variable servira à accumuler la somme des nombres que nous allons lire
S = 0

# Début d'une boucle 'for' qui va s'exécuter 10 fois
# 'range(10)' génère une séquence de nombres de 0 à 9, soit 10 nombres
for i in range(10):
    # À chaque itération, on exécute le code à l'intérieur de la boucle
    # 'input()' affiche une invite à l'utilisateur pour entrer une donnée au clavier
    # La fonction 'input()' retourne toujours une chaîne de caractères (str)
    # On convertit cette chaîne en entier avec 'int()', pour pouvoir faire des opérations mathématiques dessus
    s = int(input())
    
    # On ajoute la valeur de 's' (l'entier entré par l'utilisateur) à la variable 'S'
    # L'opérateur '+=' est un raccourci pour 'S = S + s'
    S += s

# Après la fin de la boucle (après avoir demandé 10 nombres), on affiche la valeur accumulée dans 'S'
# 'print()' sert à afficher une sortie sur la console
print(S)