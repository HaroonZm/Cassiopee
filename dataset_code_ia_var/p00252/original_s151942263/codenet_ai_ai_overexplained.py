# Demande à l'utilisateur de saisir trois valeurs séparées par des espaces sur une seule ligne.
# La fonction input() lit la ligne entrée au clavier sous forme de chaîne de caractères (string).
# La méthode split() découpe la chaîne en sous-chaînes selon les espaces et renvoie une liste de chaînes.
# Les trois variables a, b et c récupèrent respectivement la première, la deuxième et la troisième valeur saisies.
a, b, c = input().split()

# Convertit la variable a de chaîne de caractères à un nombre entier avec int().
# Cette conversion fonctionne si a est bien un nombre dans la chaîne initiale.
a = int(a)

# Convertit la variable b de chaîne de caractères à un nombre entier avec int().
b = int(b)

# Convertit la variable c de chaîne de caractères à un nombre entier avec int().
c = int(c)

# Vérifie plusieurs conditions pour décider quel message afficher.
# La structure if-elif-else permet d'exécuter un seul bloc en fonction de la première condition vraie.

# Première condition :
# On teste si la variable a vaut exactement 1 (égalité, opérateur ==)
# ET (mot-clé and pour que les deux conditions soient vraies en même temps)
# la variable b vaut aussi exactement 1
# ET la variable c vaut exactement 0
if a == 1 and b == 1 and c == 0:
    # Si toutes les conditions précédentes sont réunies, affiche le texte "Open" à l'écran.
    print("Open")
# Deuxième condition :
# On teste si a vaut 0 ET b vaut 0 ET c vaut 1
elif a == 0 and b == 0 and c == 1:
    # Si cette combinaison de valeurs est vraie, affiche aussi "Open".
    print("Open")
# Si aucune des conditions précédemment testées n'est vraie
else:
    # Affiche "Close" comme message par défaut.
    print("Close")