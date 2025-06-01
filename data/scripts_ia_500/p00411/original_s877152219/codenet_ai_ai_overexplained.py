# Demander à l'utilisateur de saisir une ligne de texte via le clavier
# La fonction input() attend que l'utilisateur entre une chaîne de caractères et appuie sur Entrée
# La méthode split() appliquée à cette chaîne découpe la chaîne en plusieurs sous-chaînes basé sur les espaces par défaut
# Cela produit une liste de chaînes de caractères représentant des nombres dans ce cas
# La fonction map() applique une fonction à chaque élément d'un iterable, ici la fonction int() convertit chaque chaîne en entier
# list() transforme le résultat, qui est un objet itérable map, en une liste concrète d'entiers
# Enfin, on affecte chacun de ces entiers à trois variables distinctes : a, t, r
a, t, r = list(map(int, input().split()))

# Calculer la valeur de la variable ans
# La multiplication r * t est effectuée en premier, conformément à la priorité des opérateurs
# Puis cette valeur est divisée par a
# Le résultat est un nombre à virgule flottante (float) par défaut puisque la division en Python 3 retourne un float
ans = r * t / a

# Afficher le résultat de ans avec une précision fixe de 6 chiffres après la virgule
# La méthode format() prend une chaîne de format "{:.6f}" qui signifie "format flottant avec 6 décimales"
# print() affiche la chaîne résultante dans la console standard suivi d'un saut de ligne
print("{:.6f}".format(ans))