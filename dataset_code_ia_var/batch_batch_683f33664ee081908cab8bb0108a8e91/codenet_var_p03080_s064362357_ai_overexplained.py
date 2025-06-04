# Appel de la fonction input() sans stocker le résultat.
# On utilise souvent cette ligne pour forcer la lecture d'une entrée,
# par exemple pour ignorer ou passer une ligne dans certains contextes (comme des titres).
input()

# On demande une saisie utilisateur via le clavier grâce à la fonction input().
# Cette saisie est ensuite stockée dans la variable s pour être utilisée plus tard.
s = input()

# On utilise la méthode count() sur la chaîne s.
# .count("R") retourne le nombre d'occurrences du caractère "R" dans s.
# .count("B") fait la même chose pour le caractère "B".
# On compare ces deux quantités grâce à l'opérateur > (supérieur à).
if s.count("R") > s.count("B"):
    # Si le nombre de "R" est strictement supérieur au nombre de "B" dans la chaîne s,
    # on entre dans ce bloc et on exécute print("Yes").
    # La fonction print() affiche le texte 'Yes' à l'écran.
    print("Yes")
else:
    # Sinon, c'est-à-dire si le nombre de "R" n'est pas strictement supérieur au nombre de "B"
    # (donc si "R" est égal ou inférieur), on exécute ce bloc.
    # La fonction print() affiche alors le texte 'No' à l'écran.
    print("No")