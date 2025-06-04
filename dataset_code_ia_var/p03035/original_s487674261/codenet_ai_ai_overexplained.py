# Demande à l'utilisateur de saisir une ligne de texte, puis divise cette ligne en une liste de sous-chaînes en utilisant l'espace (par défaut) comme séparateur.
# Par exemple, si l'utilisateur entre "12 1000", la variable input contiendra ["12", "1000"].
input = input().split()

# Ici, 'input' est une liste de chaînes de caractères, chaque élément représentant un nombre sous forme de chaîne.
# On parcourt chaque élément de cette liste en utilisant une compréhension de liste pour le convertir en entier.
# Cela crée une nouvelle liste 'listInt' contenant les mêmes valeurs, mais sous forme d'entiers.
listInt = [int(i) for i in input]

# La structure conditionnelle suivante permet de réaliser différents traitements en fonction de la valeur du premier nombre de la liste.
# On accède au premier élément de la liste 'listInt' en utilisant l'index [0].
if listInt[0] >= 13:
    # Si la valeur du premier élément est supérieure ou égale à 13,
    # on affiche simplement la valeur du second élément,
    # accessible via l'index [1].
    print(listInt[1])
elif listInt[0] > 5:
    # Si la condition précédente n'est pas respectée, mais que la valeur du premier élément est strictement supérieure à 5,
    # on effectue une division entière du second élément par 2.
    # Le résultat est converti en entier (même si la division avec '/' retourne un flottant),
    # puis affiché avec la fonction print().
    print(int(listInt[1] / 2))
else:
    # Si aucune des deux conditions précédentes n'est respectée (donc si le premier élément est inférieur ou égal à 5),
    # on affiche la valeur 0 avec print().
    print(0)