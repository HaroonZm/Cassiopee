# Création d'une liste appelée 'train' qui va contenir 2 éléments
# La liste sera remplie avec des entiers que l'utilisateur va saisir au clavier via la fonction input()
# La boucle for va s'exécuter deux fois, parce que range(2) génère une séquence de deux valeurs, 0 et 1
# Pour chaque itération, input() lit une chaîne depuis l'entrée standard (typiquement le clavier)
# La fonction int() convertit cette chaîne de caractères en un entier
# L'opération complète [int(input()) for _ in range(2)] est appelée une "compréhension de liste" qui va produire une liste en une seule ligne
train = [int(input()) for _ in range(2)]

# Création d'une autre liste appelée 'bus' qui va aussi contenir 2 éléments saisis par l'utilisateur
# Même logique que pour la liste 'train' : deux itérations, chaque fois input converti en entier, stocké dans la liste
bus = [int(input()) for _ in range(2)]

# La fonction min() prend une liste d'éléments (dans ce cas, des entiers) et renvoie l'élément le plus petit de cette liste
# min(train) récupère le plus petit des deux nombres saisis pour les trains
# min(bus) récupère le plus petit des deux nombres saisis pour les bus
# On additionne ensuite ces deux valeurs, ce qui donne la somme du plus petit nombre "train" et du plus petit nombre "bus"
# print() sert à afficher le résultat final dans la console, à l'utilisateur
print(min(train) + min(bus))