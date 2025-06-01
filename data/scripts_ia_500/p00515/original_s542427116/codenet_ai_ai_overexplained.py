from statistics import mean  # On importe la fonction 'mean' depuis le module 'statistics'. Cette fonction permet de calculer la moyenne arithmétique d'une liste de nombres.

# Déclaration d'une liste nommée 'scores'. 
# Cette liste est créée par une compréhension de liste, qui est une façon concise de construire une liste en une seule ligne.
# La compréhension fonctionne ainsi : pour chaque 'i' dans la plage de nombres allant de 0 à 4 (car range(5) génère 5 nombres: 0,1,2,3,4),
# on va demander à l'utilisateur d'entrer une valeur via la fonction input().
# Le résultat de input() est une chaîne de caractères (string), donc on utilise int() pour convertir cette chaîne en un entier.
# Chaque entier obtenu est ensuite stocké dans la liste 'scores'.
scores = [int(input()) for i in range(5)]

# On modifie la liste 'scores' en appliquant la fonction 'map'.
# map applique une fonction donnée à chaque élément de la liste.
# La fonction donnée ici est une fonction lambda (fonction anonyme, définie sans nom) qui prend un argument 'x'.
# Pour chaque élément 'x' de la liste 'scores', on calcule max(40, x).
# max(40, x) retourne la valeur la plus grande entre 40 et x.
# Cela signifie que si x est inférieur à 40, la valeur retournée sera 40, sinon ce sera x.
# Donc, cette opération remplace toute valeur inférieure à 40 par 40.
# La fonction map retourne un itérable, donc on utilise list() pour convertir cela à nouveau en liste et on réassigne à 'scores'.
scores = list(map(lambda x: max(40, x), scores))

# Enfin, on calcule la moyenne des valeurs dans 'scores' en utilisant la fonction 'mean' importée précédemment.
# La moyenne est la somme de tous les éléments divisée par le nombre d'éléments.
# On affiche cette moyenne à l'aide de la fonction 'print', qui affiche le résultat à l'écran.
print(mean(scores))