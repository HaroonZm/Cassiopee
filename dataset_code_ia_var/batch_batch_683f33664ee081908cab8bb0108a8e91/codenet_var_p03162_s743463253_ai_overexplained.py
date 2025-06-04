# Demande à l'utilisateur d'entrer un entier 'n' via l'entrée standard (habituellement le clavier)
n = int(input())  # La fonction input() lit une ligne d'entrée sous forme de chaîne de caractères, int() convertit cette chaîne en entier

# Initialisation des trois variables x, y, z à 0
# Ces variables serviront à garder en mémoire les valeurs maximales atteignables pour chaque "chemin" possible
x, y, z = 0, 0, 0  # L'affectation multiple permet de donner plusieurs variables en une seule ligne

# Cette boucle for va s'exécuter 'n' fois, c'est-à-dire une fois pour chaque ligne d'entrée supplémentaire
# Le caractère de soulignement (_) est utilisé ici comme nom de variable conventionnel pour signifier que la variable de boucle ne sera pas utilisée dans le corps de la boucle
for _ in range(n):
    # Ici, l'utilisateur va entrer trois entiers, séparés par des espaces, qui seront lus sous forme de chaîne
    # input().split() divise la chaîne d'entrée en une liste de sous-chaînes en utilisant l'espace comme séparateur
    # map(int, ...) applique la fonction int à chaque élément de la liste, les transformant en entiers
    # Les trois entiers lus sont affectés respectivement à a, b et c
    a, b, c = map(int, input().split())
    
    # À chaque itération, on calcule les nouvelles valeurs possibles pour x, y et z :
    # x : on choisit le maximum entre y et z, puis on ajoute a au résultat
    # y : on choisit le maximum entre x et z, puis on ajoute b au résultat
    # z : on choisit le maximum entre x et y, puis on ajoute c au résultat
    # Cela permet de s'assurer que pour chaque "chemin", on additionne le score du choix courant
    # tout en s'appuyant toujours sur la meilleure option précédente, sans répéter le même choix qu'au tour d'avant
    # ATTENTION : on met à jour x, y, z en une seule ligne pour utiliser les anciennes valeurs avant qu'elles ne soient modifiées
    x, y, z = a + max(y, z), b + max(x, z), c + max(x, y)

# Enfin, on affiche (avec la fonction print()) la plus grande des trois valeurs finales x, y et z
# Cela donne le score maximum total qu'on peut obtenir après avoir fait un choix à chaque étape
print(max(x, y, z))  # max(x, y, z) retourne le plus grand des trois nombres, qui est alors affiché sur la sortie standard