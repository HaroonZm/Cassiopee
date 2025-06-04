# Demande à l'utilisateur d'entrer une ligne de texte contenant deux valeurs séparées par un espace.
# raw_input() lit la saisie de l'utilisateur sous forme de chaîne de caractères (par exemple : "4 8").
# split() divise cette chaîne en une liste de sous-chaînes, en utilisant les espaces comme séparateur (ex : ["4", "8"]).
# map(int, ...) applique la fonction int à chaque élément de la liste pour les convertir de chaînes de caractères à entiers (ex : [4, 8]).
# Les deux entiers résultants sont affectés respectivement aux variables a et b.
a, b = map(int, raw_input().split())

# Commence une structure conditionnelle (if-elif-else) pour comparer les deux entiers a et b.
if a < b:
    # La condition ci-dessus vérifie si a est strictement inférieur à b.
    # Si c'est le cas, exécuté cette ligne :
    print "a < b"
elif a > b:
    # elif signifie "else if". 
    # Cette condition est testée uniquement si la précédente (a < b) est fausse.
    # Ici, on vérifie si a est strictement supérieur à b.
    print "a > b"
else:
    # else couvre tous les autres cas non couverts par les conditions précédentes, c’est-à-dire ici : a égal à b.
    print "a == b"