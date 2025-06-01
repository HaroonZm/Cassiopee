import math  # Importe la bibliothèque mathématique pour utiliser des fonctions mathématiques avancées telles que ceil

# Prend une ligne d'entrée depuis l'utilisateur, qui doit contenir deux nombres entiers séparés par un espace
# La fonction input() permet de récupérer une chaîne de caractères depuis l'entrée standard (souvent le clavier)
# La méthode split() divise cette chaîne en une liste de sous-chaînes, ici à chaque espace rencontré
# La fonction map applique la fonction int à chaque élément de cette liste pour les convertir en entiers
# Enfin, on déstructure le résultat dans deux variables n et k qui seront donc des entiers
n, k = map(int, input().split())

ret = 1  # Initialise une variable compteur 'ret' à 1, représentant ici un nombre d'étapes ou une quantité cumulée
acc = 1  # Initialise une variable d'accumulation 'acc' également à 1 ; elle va servir à suivre une somme progressive

# Démarre une boucle infinie dans laquelle on va effectuer un calcul jusqu'à ce qu'une condition de sortie soit remplie
while True:
    # Calcul de la quantité désirée 'want' à ajouter à l'accumulateur lors de chaque itération
    # math.ceil arrondit à l'entier supérieur l'opération acc/k, ce qui permet d'éviter une division partielle
    want = math.ceil(acc / k)

    # Vérification d'une condition de terminaison pour la boucle
    # On souhaite arrêter la boucle si la somme actuelle 'acc' plus la quantité à ajouter 'want' dépasse un seuil 'n'
    if (want + acc > n):
        break  # Sort de la boucle while si la condition est vraie

    # Sinon, on ajoute la quantité désirée à l'accumulateur pour mettre à jour notre somme progressive
    acc += want

    # On incrémente le compteur 'ret' de 1 pour signaler qu'une étape supplémentaire a été validée
    ret += 1

# Une fois la boucle terminée, on affiche la valeur finale du compteur ret
# La fonction print écrit cette valeur suivie d'un saut de ligne sur la sortie standard (écran)
print(ret)