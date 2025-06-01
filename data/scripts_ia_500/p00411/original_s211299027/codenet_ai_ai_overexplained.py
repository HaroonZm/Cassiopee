# La fonction "input()" permet de récupérer une chaîne de caractères saisie par l'utilisateur au clavier.
# La méthode "split()" appliquée à cette chaîne découpe cette chaîne en une liste de sous-chaînes,
# en séparant la chaîne originale à chaque espace rencontré.
# Par exemple, si l'utilisateur saisit "3 4 5", input().split() renverra la liste ["3", "4", "5"].
# La fonction "map()" applique une fonction donnée à chaque élément d'un itérable.
# Ici, la fonction appliquée est "int", qui convertit une chaîne de caractères en un entier.
# Donc, map(int, input().split()) convertit chaque élément de la liste de chaînes en un entier.
# Ensuite, on utilise le déballage multiple pour affecter ces trois entiers aux variables a, t et r respectivement.
a, t, r = map(int, input().split())

# Ici, on effectue un calcul mathématique.
# On divise r par a, ce qui donne un résultat en nombre à virgule flottante (float) car la division en Python 3 produit un float.
# Puis on multiplie ce résultat par t.
# Enfin, on utilise la fonction print() pour afficher le résultat à l'écran.
print(r / a * t)